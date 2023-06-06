from pydantic import BaseModel, validator


class Email(BaseModel):
    value: str

    @validator("value")
    def check_format(cls, v):
        """ @が含まれていない場合は例外を送出する
        """
        if "@" not in v:
            raise ValueError("メールアドレスのフォーマットが正しくありません")
        return v
