from domain.book_aggregate.book import Book, BookIsAlreadyBorrowedException

from typing import List


class BookIsAlreadyBorrowedError(Exception):
    # 本が貸出中の場合に投げる例外
    pass


class BorrowBookUseCase:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id):
        """ 本を貸し出す
        """
        # 本を取得する
        book_entity = self.book_repository.find_by_id(book_id=book_id)
        try:
            # 本を貸し出す
            book_entity.borrow()
        except BookIsAlreadyBorrowedException as e:
            raise BookIsAlreadyBorrowedError() from e
        # 本を永続化する
        self.book_repository.store(book=book_entity)
