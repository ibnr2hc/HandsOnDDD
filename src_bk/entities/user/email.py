class Email:
    def __init__(self, email: str):
        self.validate(email)
        self.value = email

    def validate(self, email: str):
        # "@"が含まれていない場合はFalseを返す
        if "@" not in email:
            raise ValueError("Email is invalid")
        self.value = email
