from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import Company_list




class CompanyForm(FlaskForm):
    """
    Form for users to create new account
    """
    names_one = StringField('Нэршил 1')
    names_two = StringField('Нэрршил 2')
    names_three = StringField('Нэршил 3')
    branches = StringField('Нэршил 4')
    submit = SubmitField('Нэмэх')