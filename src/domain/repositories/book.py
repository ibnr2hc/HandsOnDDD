from domain.entities import Book
from domain.value_object import Title, Status, BookStatus

from typing import List


class BookRepository:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def get_all_books(self) -> List[Book]:
        """ すべての書籍を返す

        Returns:
            (List[Book]): 本のリスト
        """
        # DBからすべての書籍レコードを取得
        self.db_cursor.execute("SELECT * FROM books")
        db_books = self.db_cursor.fetchall()

        for book in db_books:
            print(book, flush=True)

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
        title = Title(value=db_book["title"])
        status = Status(value=BookStatus(db_book["status"]))
        return Book(id=db_book["id"], title=title, status=status)
