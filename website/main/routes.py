from flask import request, flash, redirect, url_for, render_template, Blueprint
from website.main.forms import JunkMailForm, ImageClassifierForm
from models.junk_mail import predict_junk
from models.image_classification import predict_image
import json

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

def percent(n):
    return round(n * 100, 1)

@main.route("/image", methods=['GET', 'POST'])
def image():
    form = ImageClassifierForm()
    if request.method == "POST" and form.validate():
        result = predict_image(form.content.data)[0]
        dog, dolphin, elephant, lizard = result
        if max(result) == dog:
            name = "a dog"
        elif max(result) == dolphin:
            name = "a dolphin"
        elif max(result) == elephant:
            name = "an elephant"
        else:
            name = "a lizard"
        return render_template(
            'classifier_result.html', title="Image AI", name=name, conf=percent(max(result)),
            dog=percent(dog), dolphin=percent(dolphin), elephant=percent(elephant), lizard=percent(lizard)
        )
    return render_template('image_classifier.html', title="Image AI", form=form)
