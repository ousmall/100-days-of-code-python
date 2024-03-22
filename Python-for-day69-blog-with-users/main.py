from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from hashlib import md5


# CREATE GRAVATAR MANUALLY
def gravatar(email, size=100, default='identicon', rating='g'):
    email_hash = md5(email.lower().encode()).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default}&r={rating}"
    return gravatar_url


# CREATE A DECORATOR TO RESTRICT USAGE TO OTHER USERS
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function


# CREATE A DECORATOR TO DEFINE ONLY COMMENTER CAN DELETE COMMENT
def only_commenter(function):
    @wraps(function)
    def check(*args, **kwargs):
        user = db.session.execute(db.select(Comment).where(Comment.author_id == current_user.id)).scalar()
        if not current_user.is_authenticated or current_user.id != user.author_id:
            return abort(403)
        return function(*args, **kwargs)
    return check


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# TODO: Configure Flask-Login
# CREATE LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CONFIGURE TABLES
# Make a relationship between User and BlogPost
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
class BlogPost(db.Model):
    __tablename__ = "blog_posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # 'MANY' for table User
    # Specify author_id as a foreign key and associate it to the id column of the table User
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    # Define the relationship with the table User via posts
    author: Mapped[str] = relationship("User", back_populates="posts")

    # 'ONE' for table Comment
    comments = relationship("Comment", back_populates="comment_post")


# TODO: Create a User table for all your registered users.
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))

    # Define the relationship with the table BlogPost & Comment via author
    # 'ONE' for table BlogPost
    posts = relationship("BlogPost", back_populates="author")

    # 'ONE' for table Comment
    comments = relationship("Comment", back_populates="comment_author")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Comment(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    # Text represents a text data type in the database.
    # In most relational databases, the Text type is used to store longer text data
    # without a length limit.

    # 'MANY' for table User
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    comment_author: Mapped[str] = relationship("User", back_populates="comments")

    # 'MANY' for table BlogPost
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("blog_posts.id"))
    comment_post: Mapped[str] = relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email has already been registered, Login instead!')
            return redirect(url_for('login'))
        else:
            new_user = User(
                username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Invalid Email, Please register first.')
            return redirect(url_for('login'))

        if not check_password_hash(user.password, password):
            flash('Invalid Password, Please try again.')
            return redirect(url_for('login'))

        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Only registered users can post comments')
            return redirect(url_for('login'))
        else:
            new_comment = Comment(
                text=comment_form.text.data,
                comment_author=current_user,
                comment_post=requested_post
            )
            db.session.add(new_comment)
            db.session.commit()

    # add gravatar:
    user = current_user
    gravatar_urls = {comment.comment_author.id: gravatar(comment.comment_author.email)
                     for comment in requested_post.comments}

    return render_template("post.html", post=requested_post,
                           logged_in=current_user.is_authenticated, form=comment_form,
                           user=user, gravatar_urls=gravatar_urls)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, logged_in=current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, logged_in=current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/delete/comment/<int:comment_id>/<int:post_id>")
@only_commenter
def delete_comment(post_id, comment_id):
    post_to_delete = db.get_or_404(Comment, comment_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('show_post', post_id=post_id))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
