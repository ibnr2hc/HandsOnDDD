from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"

class Status:
    def __init__(self, status: BookStatus):
        self.validate(status)
        self.value = status

    def validate(self, status: BookStatus):
        # statusがBookStatusに含まれていない場合はFalseを返す
        if status not in BookStatus:
            raise ValueError("ステータスが不正です")
        self.value = status
