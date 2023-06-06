from infrastructure.repository.book import BookRepository
from infrastructure.repository.library import LibraryRepository
from application.usecase import BookListUseCase
from infrastructure.adapter import MySQLDatabase

from flask import Flask, render_template
app = Flask(__name__)

# リポジトリとユースケースを初期化
db_session = MySQLDatabase(host="db", user="root", password="root", dbname="library").connect()
# Repository
book_repository = BookRepository(db_cursor=db_session.cursor(dictionary=True, buffered=True))
library_repository = LibraryRepository(book_repository)
# Usecase
book_list_usecase = BookListUseCase(library_repository)


@app.route('/books', methods=['GET'])
def book_list():
    """ 本の一覧を表示する
    """
    book_dto_list = book_list_usecase.execute()
    return render_template("book_list.html", books=book_dto_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
