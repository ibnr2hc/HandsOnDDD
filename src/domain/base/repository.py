from abc import ABCMeta


class Repository(metaclass=ABCMeta):
    """リポジトリの基底クラス

    ドメイン層のリポジトリインターフェースクラスを定義する際に継承する。
    メソッドについては以下のルールで定義する。
    - 抽象メソッドとし、リポジトリ実装クラスでメソッドを実装していない場合にエラーが発生するようにする。

    例:
    @abstractmethod
    def find(self):
    """
