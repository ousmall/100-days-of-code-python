from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# Create database
class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

# Create Extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with Extension
db.init_app(app)


# Create Table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


# Website
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        if request.form:
            new_book = Book(title=request.form["title"],
                            author=request.form["author"],
                            rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        if request.form:
            new_rating = request.form['rating']
            book_id = request.form['id']
            # get id value from 'rating_edit.html', the hidden input
            book_to_update = db.get_or_404(Book, book_id)  # find a row by id
            book_to_update.rating = new_rating
            db.session.commit()
            return redirect(url_for('home'))
    book_id = request.args.get('id')
    # get id value from url after '?', and the value comes from db
    current_book = db.get_or_404(Book, book_id)
    return render_template("rating_edit.html", book=current_book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
