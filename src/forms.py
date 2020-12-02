from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

class UserInfoForm(FlaskForm):
    individual_name = StringField('Individual name: ', validators=[DataRequired()])
    project_name = StringField('Project name: ', validators=[DataRequired()])
    project_category_name = SelectField('Project category: ', validators=[DataRequired()], choices=[('web_development', 'Website Development'), ('security', 'Security')])    
    submit = SubmitField('continue')

class FeedbackForm(FlaskForm):
    question_1 = RadioField('Question 1', choices=[('one', '1'), ('two', '2'), ('three', '3'), ('three', '4'), ('three', '5')])
    question_2 = RadioField('Question 2', choices=[('one', '1'), ('two', '2'), ('three', '3'), ('three', '4'), ('three', '5')])
    question_3 = RadioField('Question 3', choices=[('yes'), ('no')])
    submit = SubmitField('submit')