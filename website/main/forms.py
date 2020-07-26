from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class JunkMailForm(FlaskForm):
    content = TextAreaField('Email Content',
        validators=[DataRequired(),
        Length(min=20, max=10000)])
    submit = SubmitField('Detect')

class ImageClassifierForm(FlaskForm):
    category = SelectField('Image Category',
        choices=[('animal', 'Animal'), ('object', 'Common Object')],
        validators=[DataRequired()])
    image = FileField('Image File',
        validators=[DataRequired(),
        FileAllowed(['jpg', 'jfif', 'png'])])
    submit = SubmitField('Detect')