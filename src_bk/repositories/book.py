from ..entities.book.book import Book, Title, Status

from typing import List


class BookRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_books(self) -> List[Book]:
        """ すべての書籍を返す

        Returns:
            (List[Book]): 本のリスト
        """
        # DBからすべての書籍レコードを取得
        db_books = self.db_session.query("SELECT * FROM books")

        # DBのレコードからドメインエンティティのBookを作成
        books = [self._db_to_entity(db_book) for db_book in db_books]
        return books

    def _db_to_entity(self, db_book) -> Book:
        """ DBのレコードから本エンティティを作成して返す

        Args:
            db_book: DBの書籍レコード
        Returns:
            (Book): 本エンティティ
        """
        # TODO: タイトルなどのvalidate結果に応じて例外処理をする
        title = Title(db_book.title)
        status = Status(db_book.status)
        return Book(db_book.id, title, status)
