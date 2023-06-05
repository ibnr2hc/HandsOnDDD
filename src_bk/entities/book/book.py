from . import Title
from ..borrowing_history.borrowing_history import BorrowingHistory

from typing import List


class Book:
    def __init__(self, id: int, title: Title, borrowing_history: List[BorrowingHistory] = []):
        self.id = id
        self.title = title
        self.borrowing_history = []

    def is_borrowed(self):
        """ 貸出中であればTrueを返す
        """
        # 貸出履歴が存在し、かつ最新の貸出履歴の返却日がNoneの場合はTrueを返す
        return bool(self.borrowing_history) and self.borrowing_history[-1].return_date is None

    def borrow_book(self, user: User):
        """ 本を借りる

        Args:
            user (User): 本を借りる利用者
        """
        # 本が貸出中でない場合は貸出履歴を追加する
        if not self.is_borrowed():
            new_history = BorrowingHistory(len(self.borrowing_history) + 1, user, self, date.today().strftime("%Y-%m-%d"))
            self.borrowing_history.append(new_history)
        # TODO: 本が貸出中の場合は例外を投げる

    def return_book(self, user: User):
        """ 本を返す

        Args:
            user (User): 本を返す利用者
        """
        # 本が貸出中の場合は貸出履歴の返却日を更新する
        if self.is_borrowed():
            self.borrowing_history[-1].return_date = date.today().strftime("%Y-%m-%d")
        # TODO: 本が貸出中でない場合は例外を投げる
