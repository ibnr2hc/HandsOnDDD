class Title:
    def __init__(self, title: str):
        self.validate(title)
        self.value = title

    def validate(self, title: str):
        # 文字数が50文字を超える場合はFalseを返す
        if len(name) > 50:
            raise ValueError("文字数が50文字を超えています")
