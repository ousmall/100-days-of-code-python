from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# render files such html must be in templates folder
# static files such as photo, CSS, videos must be in templates folder
