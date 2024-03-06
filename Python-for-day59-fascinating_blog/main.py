from flask import Flask, render_template
import requests as rs
from datetime import datetime as dt

ARTICLE = "https://api.npoint.io/886b0c394633b04e2704"

response = rs.get(url=ARTICLE)
article_post = response.json()


app = Flask(__name__)


year = dt.now().year


@app.route('/')
def home():
    return render_template("index.html", posts=article_post, current_year=year)


@app.route('/blog/<int:index>')
def blogs(index):
    return render_template("post.html", posts=article_post, index=index, current_year=year)


@app.route('/contact')
def contact():
    return render_template("contact.html", current_year=year)


@app.route('/about')
def self_information():
    return render_template("about.html", current_year=year)


if __name__ == "__main__":
    app.run(debug=True)
