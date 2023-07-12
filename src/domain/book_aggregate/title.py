from pydantic import validator
from domain.base.value_object import ValueObject

class Title(ValueObject):
    value: str

    @validator("value")
    def check_length(cls, v):
        """ 文字数が50文字を超える場合は例外を送出する
        """
        if len(v) > 50:
            raise ValueError("文字数が50文字を超えています")
        return v
