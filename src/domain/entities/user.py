from domain.value_object import Email, Name

class User:
    def __init__(self, id: int, name: Name, email: Email):
        self.id = id
        self.name = name
        self.email = email