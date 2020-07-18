from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class JunkMailForm(FlaskForm):
    content = TextAreaField('Email Content', validators=[DataRequired(), Length(min=20, max=10000)])
    submit = SubmitField('Detect')