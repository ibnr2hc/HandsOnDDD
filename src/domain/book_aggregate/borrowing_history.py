from domain.base.entity import Entity

class BorrowingHistory(Entity):
    def __init__(self, id: int, user: 'User', book: 'Book', borrow_date: str, due_date: str, return_date: str):
        self.id = id
        self.user = user
        self.book = book
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
