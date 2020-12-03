from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

# Add a "any more comments?" field

class UserInfoForm(FlaskForm):
    individual_name = StringField('Individual name: ', validators=[DataRequired()])
    business_name = StringField('Business name: ', validators=[DataRequired()])
    project_category_name = SelectField('Project category: ', validators=[DataRequired()], choices=[('web development', 'Website Development'), ('security', 'Security')])    
    submit = SubmitField('continue')

class FeedbackForm(FlaskForm):
    question_1 = RadioField('Question 1', choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')])
    question_2 = RadioField('Question 2', choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')])
    question_3 = RadioField('Question 3', validators=[DataRequired()],  choices=[('yes'), ('no')])
    submit = SubmitField('submit')