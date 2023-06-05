from repositories.book_repository import BookRepository
from repositories.library_repository import LibraryRepository
from usecases.list_books import BookListUseCase

from flask import Flask, render_template
app = Flask(__name__)

# リポジトリとユースケースを初期化
db_session = get_db_session()  # TODO: 定義する
# Repository
book_repository = BookRepository(db_session)
library_repository = LibraryRepository(book_repository)
# Usecase
book_list_usecase = BookListUseCase(library_repository)


@app.route('/books', methods=['GET'])
def book_list():
    """ 本の一覧を表示する
    """
    book_dto_list = book_list_usecase.execute()
    return render_template('book_list.html', book_list=book_list)


if __name__ == '__main__':
    app.run()
