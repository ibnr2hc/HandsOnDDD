from domain.book_aggregate.book import Book
from domain.book_aggregate.title import Title
from domain.book_aggregate.status import Status, BookStatus
from domain.base.repository import Repository

from typing import List


class BookRepository(Repository):
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def store(self, book: Book):
        """ 本を更新する

        Args:
            book (Book): 更新する本
        """
        # DBの書籍レコードを更新
        # TODO: Entityの属性が増えた場合にも対応しやすい作りにする
        if book.id is None:  # 新規作成の場合
            self.db_cursor.execute("INSERT INTO books (title, status) VALUES (%s, %s)", (book.title.value, book.status.value.value))
        else:  # 更新の場合
            self.db_cursor.execute("UPDATE books SET title = %s, status = %s WHERE id = %s", (book.title.value, book.status.value.value, book.id))

    def find_by_id(self, book_id) -> Book:
        """ IDに一致する本を返す

        Args:
            book_id (int): 本のID
        Returns:
            (List[Book]): 本のリスト
        """
        # DBからIDに一致する書籍レコードを取得
        # TODO: レコードが存在しない場合のエラー処理
        self.db_cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        db_book = self.db_cursor.fetchone()

        # DBのレコードからドメインエンティティのBookを作成
        return self._db_to_entity(db_book)

    def find_all(self) -> List[Book]:
        """ すべての書籍を返す

        Returns:
            (List[Book]): 本のリスト
        """
        # DBからすべての書籍レコードを取得
        self.db_cursor.execute("SELECT * FROM books")
        db_books = self.db_cursor.fetchall()

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
