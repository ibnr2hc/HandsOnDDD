from ..entities.book import Book

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
        return self._books_entity_to_dto(books=library.list_books())

    def _books_entity_to_dto(self, books: List[Book]) -> List[BookDTO]:
        """ 本のエンティティのリストをBookDTOのリストに変換する

        Args:
            books (List[Book]): 本のエンティティのリスト
        Returns:
            (List[BookDTO]): 本のDTOのリスト
        """
        book_dto_list = []
        for book in books:
            book_dto_list.append(BookDTO(book))
        return book_dto_list

# TODO: 責務的に別の層がいいかも
class BookDTO:
    def __init__(self, book):
        self.id = book.id
        self.title = book.title.value
        self.is_borrowed = book.is_borrowed()
