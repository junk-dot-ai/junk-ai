from flask import request, flash, redirect, url_for, render_template, Blueprint
from website.main.forms import JunkMailForm
from models.junk_mail.junk_mail import predict_junk


main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template('home.html', title="Home")

@main.route("/text", methods=['GET', 'POST'])
def text():
    form = JunkMailForm()
    if request.method == "POST" and form.validate():
        if (predict_junk(form.content.data) > 0.5):
            flash("Junk!", "danger")
        else:
            flash("Not Junk!", "success")
        return redirect(url_for('main.text'))
    return render_template('junk_mail.html', title="Junk Mail AI", form=form)

@main.route("/image")
def image():
    return render_template('image_classifier.html', title="Image AI")