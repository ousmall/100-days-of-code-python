from flask import Flask, render_template
import requests as rs

ARTICLE = "https://api.npoint.io/e7400a2cffa6eed1d7c3"

response = rs.get(url=ARTICLE)
article_data = response.json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", posts=article_data)


@app.route('/blog/<int:index>')
def article(index):
    return render_template("post.html", posts=article_data, index=index)


if __name__ == "__main__":
    app.run(debug=True)
