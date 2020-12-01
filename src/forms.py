from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class UserInfoForm(FlaskForm):
    individual_name = StringField('Individual name: ', validators=[DataRequired()])