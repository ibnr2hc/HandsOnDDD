from domain.base.entity import Entity
from typing import Optional

class BorrowingHistory(Entity):
    id: Optional[int]
    user_id: int
    borrow_date: str
    return_date: Optional[str]
    # def __init__(self, user_id: int, borrow_date: str, return_date: str = None, id: int = None):
    #     self.id = id
    #     self.user_id = user_id
    #     self.borrow_date = borrow_date
    #     self.return_date = return_date
