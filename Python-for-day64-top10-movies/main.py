from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, CheckConstraint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange
import requests

TMDB_API_KEY = "you-own-one"

TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_DETAIL_URL = "https://api.themoviedb.org/3/movie/"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/original"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer you-own-one"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# create SQLite table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, CheckConstraint('rating <= 10'), nullable=True)  # score
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)  # sequence
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# I added data with DB Browser


# create flak_bootstrap form
class NewDoubleRForm(FlaskForm):
    rating = DecimalField('Your New Rating', validators=[DataRequired(),
                                                         NumberRange(min=1, max=10, message="Rating must be in "
                                                                                            "1 to 10")])
    review = StringField('Your New Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchMovieForm(FlaskForm):
    movie_title = StringField('Movie Title:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    # all() 是查询对象的方法之一，用于执行查询并返回符合查询条件的所有结果，返回的结果是一个 Python 的列表（list）
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/update", methods=['POST', 'GET'])
def edit():
    """ use flak_bootstrap form data """
    editing_form = NewDoubleRForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if editing_form.validate_on_submit():
        movie.rating = float(editing_form.rating.data)
        movie.review = editing_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=editing_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    searchform = SearchMovieForm()
    if searchform.validate_on_submit():
        movie_title = searchform.movie_title.data
        params = {"api_kei": TMDB_API_KEY, "query": movie_title}
        response = requests.get(TMDB_SEARCH_URL, headers=headers, params=params)
        data = response.json()['results']
        return render_template("select.html", movie_list=data)
    return render_template("add.html", form=searchform)


@app.route("/select")
def pick_up():
    """insert the data of user option to database"""
    movie_id = request.args.get('id')  # get data from url not the database
    if movie_id:
        detail_url = f"{TMDB_DETAIL_URL}{movie_id}"
        params = {"api_key": TMDB_API_KEY, "movie_id": movie_id}
        response = requests.get(detail_url, headers=headers, params=params)
        data = response.json()
        with app.app_context():
            new_movie = Movie(
                title=data['title'],
                year=data['release_date'].split('-')[0],
                description=data['overview'],
                img_url=f"{TMDB_IMAGE_URL}{data['poster_path']}"
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('edit', id=new_movie.id))
            # 用return redirect(url_for('edit', id=new_movie.id))来生成编辑页面的 URL，
            # 其中 id=new_movie.id 作为 URL 参数传递给 edit 视图。
            # in this case, id is "11", not the id in TMDB


if __name__ == '__main__':
    app.run(debug=True)
