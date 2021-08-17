from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, DecimalField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from web_site.models import Products

class AdminEditProductsForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(message="This must contain a proper int or float value")])
    upload_image = FileField('Upload Image', validators=[DataRequired(),FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Item')

    def validate_price(self, price):
        if price.data <= 0:
            raise ValidationError("Price has to be a positive number")
