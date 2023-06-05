class Name:
    def __init__(self, name: str):
        self.validate(name)
        self.value = name

    def validate(self, name: str):
        # 文字数が50文字を超える場合はFalseを返す
        if len(name) > 50:
            raise ValueError("文字数が50文字を超えています")
