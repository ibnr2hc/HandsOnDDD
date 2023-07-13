from domain.book_aggregate.book import Book
from application.usecase.book_list_dto import BookListDTO

from typing import List


class BookListUseCase:
    def __init__(self, library_repository):
        self.library_repository = library_repository

    def execute(self) -> List[Book]:
        """ 本の一覧を返す

        Returns:
            (List[Book]): 本Entityのリスト
        """
        # 本の一覧を取得する
        library = self.library_repository.get_library()
        return library.list_books()
