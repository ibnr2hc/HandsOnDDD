from domain.book_aggregate.book_repository import BookRepository
from domain.library_aggregate.library_repository import LibraryRepository
from application.usecase.book_list import BookListUseCase
from application.usecase.book_list_dto import BookListDTO
from application.usecase.book_detail import BookDetailUseCase
from application.usecase.book_detail_dto import BookDetailDTO
from application.usecase.update_book import UpdateBookUseCase
from application.usecase.borrow_book import BorrowBookUseCase, BookIsAlreadyBorrowedError
# TODO: MySQLという知識をこの層に流出させないようにする
from infrastructure.adapter import MySQLDatabase

from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__, template_folder="presentation/templates")
app.config['SECRET_KEY'] = 'aiueo'

# リポジトリとユースケースを初期化
db_session = MySQLDatabase(host="db", user="root", password="root", dbname="library").connect()
# Repository
book_repository = BookRepository(db_cursor=db_session.cursor(dictionary=True, buffered=True))
library_repository = LibraryRepository(book_repository=book_repository)
# Usecase
book_list_usecase = BookListUseCase(library_repository)
book_detail_usecase = BookDetailUseCase(book_repository)
update_book_usecase = UpdateBookUseCase(book_repository)
borrow_book_usecase = BorrowBookUseCase(book_repository)


@app.route('/books', methods=['GET'])
def book_list():
    """ 本の一覧を表示する
    """
    library_entity = book_list_usecase.execute()
    library_dto = BookListDTO.from_entity(library_entity)
    return render_template("book_list.html", books=library_dto)

@app.route('/books/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    """ 本の一覧を詳細を表示する
    """
    # # POSTの場合は更新処理を行う
    # if request.method == 'POST':
    #     # TODO: パラメーターの渡し方が汚いのでリファクタリングする
    #     update_book_usecase.execute(
    #         book_id=book_id,
    #         title=request.form["title"],
    #         status=request.form["status"]
    #     )
    #     flash('更新が完了しました')
    #     return redirect(url_for('book_detail', book_id=book_id))

    # GETの場合は詳細を表示する
    book_entity = book_detail_usecase.execute(book_id=book_id)
    book_dto = BookDetailDTO.entity_to_dto(book_entity)
    return render_template("book_detail.html", book=book_dto)

@app.route('/books/<int:book_id>/borrow', methods=['POST'])
def borrow_book(book_id):
    """ 本の貸し出しを行う
    """
    try:
        book_entity = borrow_book_usecase.execute(book_id=book_id)
        flash('貸出が完了しました')
    except BookIsAlreadyBorrowedError:
        flash("本が既に貸出されています")
    return redirect(url_for('book_detail', book_id=book_id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
