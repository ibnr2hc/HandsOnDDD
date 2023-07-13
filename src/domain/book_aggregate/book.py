from domain.book_aggregate.title import Title
from domain.book_aggregate.status import Status, BookStatus
from domain.book_aggregate.borrowing_history import BorrowingHistory
from domain.base.entity import Entity
from datetime import date

from typing import List


class BookIsAlreadyBorrowedException(Exception):
    # 本が貸出中の場合に投げる例外
    pass


class Book(Entity):
    id: int
    title: Title
    status: Status
    borrowing_history: List[BorrowingHistory] = []

    def change_title(self, title: Title):
        """ 本のタイトルを変更する

        Args:
            title (Title): 本のタイトル
        """
        self.title = title

    def is_borrowed(self):
        """ 貸出中であればTrueを返す
        """
        # 貸出中ステータス(=BORROWED)の場合はTrueを返す
        return self.status.value == BookStatus.BORROWED

    def borrow(self):
        """ 本を借りる
        貸出ステータスを貸出中にする

        Except:
            BookIsAlreadyBorrowedError: 本が貸出中の場合
        """
        # 本が貸出中でない場合は貸出ステータスを貸出中(=BORROWED)を追加する
        if not self.is_borrowed():
            self.status = Status(value=BookStatus.BORROWED)
        else:
            raise BookIsAlreadyBorrowedException()

    # def return(self, user_id: int):
    #     """ 本を返す

    #     Args:
    #         user_id (int): 本を返す利用者
    #     """
    #     # 本が貸出中の場合は貸出履歴の返却日を更新する
    #     if self.is_borrowed():
    #         self.borrowing_history[-1].return_date = date.today().strftime("%Y-%m-%d")
    #     # TODO: 本が貸出中でない場合は例外を投げる
