from typing import List

class BookDetailDTO:
    def __init__(self, book):
        self.id = book.id
        self.title = book.title.value
        self.status = book.status.value.value
        self.is_borrowed = book.is_borrowed()

    @staticmethod
    def from_entity(book: 'Book'):
        """ 本のエンティティをBookDTOに変換する

        Args:
            book (Book): 本のエンティティ
        Returns:
            (BookDTO): 本のDTO
        """
        return BookDetailDTO(book)


class BookListDTO:
    def __init__(self, books: List[BookDetailDTO]):
        self.books = books

    @staticmethod
    def from_entity(books: List['Book']):
        """ 本のエンティティをBookDTOに変換する

        Args:
            book (Book): 本のエンティティ
        Returns:
            (BookDTO): 本のDTO
        """
        return BookListDTO([BookDetailDTO(book) for book in books])
