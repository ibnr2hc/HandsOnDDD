class BookDetailDTO:
    def __init__(self, book):
        self.id = book.id
        self.title = book.title.value
        self.status = book.status.value.value
        self.is_borrowed = book.is_borrowed()

    @staticmethod
    def entity_to_dto(book):
        """ 本のエンティティをBookDTOに変換する

        Args:
            book (Book): 本のエンティティ
        Returns:
            (BookDTO): 本のDTO
        """
        return BookDetailDTO(book)
