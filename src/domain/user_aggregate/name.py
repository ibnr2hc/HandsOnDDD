from pydantic import BaseModel, validator


class Name(BaseModel):
    value: str

    @validator("value")
    def check_length(cls, v):
        """ 文字数が50文字を超える場合は例外を送出する
        """
        if len(v) > 50:
            raise ValueError("文字数が50文字を超えています")
        return v
