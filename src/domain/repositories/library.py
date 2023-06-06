from . import BookRepository
from domain.entities import Library


class LibraryRepository:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def get_library(self) -> Library:
        """ Libraryエンティティを返す

        Returns:
            (Library): Libraryエンティティ
        """
        books = self.book_repository.get_all_books()
        return Library(books=books)
