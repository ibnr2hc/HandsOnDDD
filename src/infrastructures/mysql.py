import mysql.connector
from mysql.connector import Error

import time


class MySQLDatabase:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self._max_retry_count = 5
        self._retry_interval = 5  # sec

    def connect(self):
        # MySQLに接続します。接続できない場合は何度かリトライします。
        for retry_count in range(self._max_retry_count):
            try:
                session = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    db=self.dbname,
                    charset="utf8",
                    use_unicode=True,
                    get_warnings=True
                )

                if session.is_connected():
                    print("MySQLに接続されました")
                    return session

            except Error as e:
                if retry_count < self._max_retry_count - 1:
                    print(f"MySQLの接続に失敗しました。再度接続を試みます。")
                    time.sleep(self._retry_interval)
                else:
                    raise e
