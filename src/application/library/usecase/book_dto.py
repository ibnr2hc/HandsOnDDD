class BookDTO:
    def __init__(self, book):
        self.id = book.id
        self.title = book.title.value
        self.status = book.status.value.value
        self.is_borrowed = book.is_borrowed()

    @staticmethod
    def from_entity(book):
        """ 本のエンティティをBookDTOに変換する

        Args:
            book (Book): 本のエンティティ
        Returns:
            (BookDTO): 本のDTO
        """
        return BookDTO(book)

    @staticmethod
    def from_entities(books):
        """ 本のエンティティのリストをBookDTOのリストに変換する

        Args:
            books (List[Book]): 本のエンティティのリスト
        Returns:
            (List[BookDTO]): 本のDTOのリスト
        """
        return [BookDTO.from_entity(book) for book in books]
