from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template('home.html')

@main.route("/text")
def text():
    return render_template('junk_mail.html')

@main.route("/image")
def image():
    return render_template('image_rec.html')