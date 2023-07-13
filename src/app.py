from domain.book_aggregate.book_repository import BookRepository
from domain.library_aggregate.library_repository import LibraryRepository
from application.usecase.list_books import BookListUseCase
from application.usecase.book_detail import BookDetailUseCase
from application.usecase.book_detail_dto import BookDetailDTO
from application.usecase.update_book import UpdateBookUseCase
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

# TODO: 本貸し出し中に何かしらの値を変更できないようにするといい勉強になりそう


@app.route('/books', methods=['GET'])
def book_list():
    """ 本の一覧を表示する
    """
    book_dto_list = book_list_usecase.execute()
    return render_template("book_list.html", books=book_dto_list)

@app.route('/books/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    """ 本の一覧を詳細を表示する
    """
    # POSTの場合は更新処理を行う
    if request.method == 'POST':
        # TODO: パラメーターの渡し方が汚いのでリファクタリングする
        book_dto = update_book_usecase.execute(book_id=book_id, title=request.form["title"])
        flash('更新が完了しました')
        return redirect(url_for('book_detail', book_id=book_id))

    # GETの場合は詳細を表示する
    book_entity = book_detail_usecase.execute(book_id=book_id)
    book_dto = BookDetailDTO.entity_to_dto(book_entity)
    return render_template("book_detail.html", book=book_dto)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
