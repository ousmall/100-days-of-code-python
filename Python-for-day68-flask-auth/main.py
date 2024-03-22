from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE LOGIN-MANAGER
# https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    # the second way to illustrate:
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100))
    # email = db.Column(db.String(100), unique=True)
    # password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# there are some contradictions when I use 'UserMixin',
# and new object 'new_user' in 'register' will show incorrect prompt "unexpected argument"
# so that we should re-initial 'class User()'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form:
            email = request.form.get('email')
            user = User.query.filter_by(email=email).first()
            if user:
                flash('This email has already been registered, Login instead!')
                return redirect(url_for('login'))

            else:
                # PBKDF2 是一个被广泛采用的密码哈希函数，并且通常是许多安全标准（如 PKCS#5）的一部分，
                # 但 Scrypt 在防止特定类型的攻击（如硬件加速攻击）方面更具优势，因此在某些情况下，更值得推荐。
                # https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security
                new_user = User(
                    name=request.form.get('name'),
                    email=request.form.get('email'),
                    password=generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
                )
                db.session.add(new_user)
                db.session.commit()

                # login after pass data to DB
                login_user(new_user)

                return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # match user
        user = User.query.filter_by(email=email).first()
        # result = db.session.execute(db.select(User).where(User.email == email))
        # user = result.scalar()

        # authentication
        if not user:
            flash('Invalid Email, Please register first.')
            return redirect(url_for('login'))

        if not check_password_hash(user.password, password):
            flash('Invalid Password, Please try again.')
            return redirect(url_for('login'))

        else:
            login_user(user)
            return redirect(url_for('secrets'))
        # https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/

    return render_template("login.html", logged_in=current_user.is_authenticated)


# Views that require your users to be logged in by decorated with the login_required decorator
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


# the same as secrets
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf')
# https://flask.palletsprojects.com/en/2.3.x/api/#flask.send_from_directory


if __name__ == "__main__":
    app.run(debug=True)
