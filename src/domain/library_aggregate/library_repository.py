from domain.book_aggregate.book_repository import BookRepository
from domain.library_aggregate.library import Library
from domain.base.repository import Repository


class LibraryRepository(Repository):
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def get_library(self) -> Library:
        """ Libraryエンティティを返す

        Returns:
            (Library): Libraryエンティティ
        """
        books = self.book_repository.find_all()
        return Library(books=books)
