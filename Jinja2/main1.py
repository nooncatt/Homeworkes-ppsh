from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
# sicret key это низя выкладывать на гитхаб!!!
app.config['SECRET_KEY'] = "helloworld_secret_key"


class NamerForm(FlaskForm):
    name = StringField("Имя:", validators=[DataRequired()])
    submit = SubmitField("Отправить")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    clothes = ["T-shirt", "skirt", "hat"]
    return render_template("user.html", name=name, clothes=clothes)


@app.route("/name_form", methods=["GET", "POST"])
def name_form():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name_form.html", form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)