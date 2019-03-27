from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField,SelectField,FileField,TextAreaField
from wtforms.validators import InputRequired,Email,DataRequired
from flask_wtf.file import FileRequired,FileAllowed
from wtforms.widgets import TextArea

class UploadForm(Form):
    
    desc = TextAreaField('Description', validators=[DataRequired('A message is required!')])
    image = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
