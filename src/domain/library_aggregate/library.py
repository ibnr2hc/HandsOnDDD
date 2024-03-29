from domain.base.entity import Entity
from domain.book_aggregate.book import Book
from domain.user_aggregate.user import User

from typing import List


class Library(Entity):
    books: List[Book]

    def list_books(self):
        """ 本の一覧を返す
        """
        return self.books

    def get_book_detail(self, book_id: int) -> Book:
        """ 本の詳細を返す

        Args:
            book_id (int): 本のID
        Returns:
            Book: 本の詳細
        """
        # 本のIDが一致する本を返す
        for book in self.books:
            if book.id == book_id:
                return book

    def borrow_book(self, book_id: int, user: User):
        """ 本を借りる

        Args:
            book_id (int): 本のID
            user (User): 本を借りる利用者
        """
        book_to_borrow = self.get_book_detail(book_id)
        book_to_borrow.borrow_book(user)

    def return_book(self, book_id: int, user: User):
        """ 本を返す

        Args:
            book_id (int): 本のID
            user (User): 本を返す利用者
        """
        book_to_return = self.get_book_detail(book_id)
        book_to_return.return_book(user)
