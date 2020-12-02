from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UserInfoForm(FlaskForm):
    individual_name = StringField('Individual name: ', validators=[DataRequired()])
    project_name = StringField('Project name: : ', validators=[DataRequired()])
    project_category_name =SelectField('Project category: ', validators=[DataRequired()])    
    submit = SubmitField('continue')