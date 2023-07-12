from domain.book_aggregate.book import Book
from .book_dto import BookDTO

from typing import List


class BookListUseCase:
    def __init__(self, library_repository):
        self.library_repository = library_repository

    def execute(self) -> List[BookDTO]:
        """ 本の一覧を返す

        Returns:
            (List[BookDTO]): 本のDTOのリスト
        """
        # 本の一覧を取得する
        library = self.library_repository.get_library()
        # 本の一覧をBookDTOのリストに変換する
        return BookDTO.from_entities(books=library.list_books())
