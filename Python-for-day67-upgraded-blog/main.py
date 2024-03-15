from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Initial CKEditor(add support to image upload, code syntax highlighting and more.)
ckeditor = CKEditor(app)


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# Flask-WTF/WTForms
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    bg_url = StringField('Background URL', validators=[DataRequired(), URL()], render_kw={"placeholder": "https://"})
    body = CKEditorField('Blog content', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.date))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)  # fetch one data a time by post_id
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/make-post', methods=['POST', 'GET'])
def add_new_post():
    new_form = PostForm()
    if new_form.validate_on_submit():
        # don't forget add 'data' in the end when get data from the form and post to database
        new_blog = BlogPost(
            title=new_form.title.data,
            subtitle=new_form.subtitle.data,
            date=date.today().strftime('%B %d, %y'),
            body=new_form.body.data,
            author=new_form.author.data,
            img_url=new_form.bg_url.data
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=new_form)


@app.route('/edit-post/<int:post_id>', methods=['POST', 'GET'])
def edit_post(post_id):
    # get data from database and show them in the form
    # HTML forms (WTForms included) do not accept PUT, PATCH or DELETE methods
    post_for_edit = db.get_or_404(BlogPost, post_id)
    edit_form = PostForm(
        title=post_for_edit.title,
        subtitle=post_for_edit.subtitle,
        author=post_for_edit.author,
        bg_url=post_for_edit.img_url,
        body=post_for_edit.body
    )
    # update data to database
    if edit_form.validate_on_submit():
        post_for_edit.title = edit_form.title.data
        post_for_edit.subtitle = edit_form.subtitle.data
        post_for_edit.body = edit_form.body.data
        post_for_edit.author = edit_form.author.data
        post_for_edit.img_url = edit_form.bg_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_for_edit.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    post_for_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_for_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
