from domain.book_aggregate.book import Book

from typing import List


class BookDetailUseCase:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id) -> Book:
        """ 本の一覧を返す

        Returns:
            (List[BookDTO]): 本のDTOのリスト
        """
        # 本の詳細を取得する
        book = self.book_repository.find_by_id(book_id=book_id)
        # 本の一覧をBookDTOのリストに変換する
        return book
