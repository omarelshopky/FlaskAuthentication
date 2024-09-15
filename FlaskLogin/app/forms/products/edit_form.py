from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange

class EditForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=5, max=20)])
    price = FloatField("Price", validators=[DataRequired(), NumberRange(min=1)])
