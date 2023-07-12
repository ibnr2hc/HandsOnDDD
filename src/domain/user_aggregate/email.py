from domain.base.value_object import ValueObject

from pydantic import validator


class Email(ValueObject):
    value: str

    @validator("value")
    def check_format(cls, v):
        """ @が含まれていない場合は例外を送出する
        """
        if "@" not in v:
            raise ValueError("メールアドレスのフォーマットが正しくありません")
        return v
