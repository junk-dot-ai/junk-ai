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
    if form.validate_on_submit():
        if (predict_junk(form.content.data) > 0.5):
            flash("Junk!", "danger")
        else:
            flash("Not Junk!", "success")
        return redirect(url_for('main.text'))
    return render_template('junk_mail.html', title="Junk Mail AI", form=form)

@main.route("/image", methods=['GET', 'POST'])
def image():
    form = ImageClassifierForm()
    if form.validate_on_submit():
        prediction, class_to_confidence, img_b64 = predict_image(form.image.data, form.category.data)
        return render_template(
            'classifier_result.html',
            title="Image AI",
            category=form.category.data,
            prediction=prediction,
            class_to_confidence=class_to_confidence,
            image=str(img_b64, 'utf-8'),
        )
    return render_template('image_classifier.html', title="Image AI", form=form)
