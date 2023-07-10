from domain.user_aggregate.email import Email
from domain.user_aggregate.name import Name

class User:
    def __init__(self, id: int, name: Name, email: Email):
        self.id = id
        self.name = name
        self.email = email