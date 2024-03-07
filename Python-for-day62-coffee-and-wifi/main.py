from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

COFFEE_RATING = [('❌', '❌'), ('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕', '☕️☕️☕')]
WIFI_RATING = [('❌', '❌'), ('📡', '📡'), ('📡📡️', '📡📡'), ('📡📡📡', '📡📡📡')]
POWER_RATING = [('❌', '❌'), ('🔌', '🔌'), ('🔌🔌️', '🔌🔌️'), ('🔌🔌🔌', '🔌🔌🔌')]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)',
                           validators=[DataRequired(), URL()], render_kw={"placeholder": "https://"})
    open_time = TimeField('Opening Time: 24-hour e.g. 08:00', validators=[DataRequired()])
    close_time = TimeField('Closing Time: 24-hour e.g. 17:30', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=COFFEE_RATING, validators=[DataRequired()])
    wifi_rating = SelectField('Wi-Fi Rating', choices=WIFI_RATING, validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=POWER_RATING, validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_coffee = [form.data[item] for item in form.data][:7]
        cafe_list = ','.join(new_coffee)
        with open("cafe-data.csv", mode="a", encoding="utf-8", newline='') as file:
            file.write('\n' + cafe_list)
        # Clear data
        form.process()

        return redirect(url_for('add_cafe'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            list_of_length = len(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, cafes_len=list_of_length)


if __name__ == '__main__':
    app.run(debug=True)
