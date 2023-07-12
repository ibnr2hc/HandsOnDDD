from pydantic import BaseModel


class ValueObject(BaseModel):
    """値オブジェクトの基底クラス"""

    class Config:
        frozen = True  # 値オブジェクトは不変であることを保証する

