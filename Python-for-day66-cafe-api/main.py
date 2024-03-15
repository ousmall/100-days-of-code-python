import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

USER_API = "TopSecretAPIKey"


app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    #  form the data to a dict and then convert to json format
    def to_dict(self):
        # dictionary comprehension
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random_cafe():
    api_key = request.args.get("api-key")
    if api_key == USER_API:
        result = db.session.execute(db.select(Cafe))  # show data in original order
        all_cafes = result.scalars().all()
        cafe_choice = random.choice(all_cafes)
        return jsonify(cafe=cafe_choice.to_dict())


# https://www.adamsmith.haus/python/docs/flask.jsonify


@app.route("/all", methods=['GET'])
def get_all_cafes():
    api_key = request.args.get("api-key")
    if api_key == USER_API:
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name))  # show order by name
        all_cafes = result.scalars().all()
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=['GET'])
def search_cafe_location():
    api_key = request.args.get("api-key")
    if api_key == USER_API:
        location = request.args.get('location')
        result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
        all_cafes = result.scalars().all()
        if all_cafes:
            return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at the location."}), 404
        # '404' specifies the status code of the HTTP response


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    api_key = request.args.get("api-key")
    if api_key == USER_API:
        try:
            new_cate = Cafe(
                name=request.form['name'],
                map_url=request.form['map_url'],
                img_url=request.form['img_url'],
                location=request.form['location'],
                coffee_price=request.form['coffee_price'],
                seats=request.form['seats'],
                has_toilet=bool(request.form['has_toilet']),
                has_wifi=bool(request.form['has_wifi']),
                has_sockets=bool(request.form['has_sockets']),
                can_take_calls=bool(request.form['can_take_calls'])
            )
            # request.form 是 Flask 中的一个属性，用于访问客户端通过 POST 请求发送的表单数据。
        except KeyError:
            return jsonify(error={"Wrong request": "Some or all information is incorrect or missing."}), 404
        else:
            db.session.add(new_cate)
            db.session.commit()
            return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record (put: update an entire piece of data, patch: update a piece of data)
@app.route("/update_price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == USER_API:
        new_price = request.args.get("new_price")
        # cafe = db.get_or_404(Cafe, cafe_id)
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully update the new price."})
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe with that ID."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def report_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == USER_API:
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe:
            db.session.delete()
            db.session.commit()
            return jsonify(response={"success": "Successfully delete the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe with that ID."}), 404
    else:
        return jsonify(error={"Not Authorized": "Sorry, forbidden request, make sure you have correct API-KEY."}), 404


if __name__ == '__main__':
    app.run(debug=True)


# API DOCUMENT:
# https://documenter.getpostman.com/view/33592565/2sA2xk1rxG