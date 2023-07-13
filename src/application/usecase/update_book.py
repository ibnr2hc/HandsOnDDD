from domain.book_aggregate.title import Title


class UpdateBookUseCase:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def execute(self, book_id, title):
        """ 本を更新し、更新された本のDTOを返す

        Args:
            book_id (int): 本のID
            title (str): 本のタイトル
        """
        # 本の詳細を取得する
        book = self.book_repository.find_by_id(book_id=book_id)
        new_title = Title(value=title)
        book.change_title(title=new_title)

        # 本の更新を永続化する
        self.book_repository.store(book=book)
