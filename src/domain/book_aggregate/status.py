from pydantic import validator
from domain.base.value_object import ValueObject

from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"

class Status(ValueObject):
    value: BookStatus

    @validator("value")
    def check_valid_status(cls, v):
        """ statusがBookStatusに含まれていない場合は例外を送出する
        """
        if v not in BookStatus:
            raise ValueError("ステータスが不正です")
        return v
