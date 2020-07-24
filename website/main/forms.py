from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class JunkMailForm(FlaskForm):
    content = TextAreaField('Email Content', validators=[DataRequired(), Length(min=20, max=10000)])
    submit = SubmitField('Detect')

class ImageClassifierForm(FlaskForm):
    content = FileField('Image File', validators=[FileAllowed(['jpg', 'jfif', 'png'])])
    submit = SubmitField('Detect')
