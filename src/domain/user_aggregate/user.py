from domain.user_aggregate.email import Email
from domain.user_aggregate.name import Name
from domain.base.entity import Entity

class User(Entity):
    id: int
    name: Name
    email: Email
