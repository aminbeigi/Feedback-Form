from flask import render_template, url_for, redirect, session, request
from feedbackform.forms import UserInfoForm, FeedbackForm
from feedbackform import app
from feedbackform.static_config_parser import StaticConfigParser
from feedbackform.send_email import SendEmail
import feedbackform.errors

SEND_EMAIL = SendEmail()

form_content = [
    {
        'category' : 'web development',
        'question 1' : 'Quality and value of user inferfaces.',
        'question 2' : 'Features have been added as requested (i.e. buttons).',
        'question 3' : 'Do you want an extended meeting about ideas on how to further grow '
    },
    {
        'category' : 'security',
        'question 1' : 'Quality, value, and speed of secuirty services.',
        'question 2' : 'Clarity and promptness of communicating security concerns.',
        'question 3' : 'Do you want an extended meeting about ideas on how to further grow '
    }
]

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    user_form = UserInfoForm()
    if user_form.validate_on_submit():
        data = {
            'individual_name' : user_form.individual_name.data,
            'business_name' : user_form.business_name.data,
            'project_category' : user_form.project_category_name.data
        }
        session['data'] = data #session (cookie) variable
        return redirect(url_for('form', data=data))
    return render_template('home.html', user_form=user_form, form_content=form_content)

@app.route('/home/form', methods=['GET', 'POST'])
def form():
    body = ''
    data = request.args['data']  # counterpart for url_for()
    data = session['data']       # counterpart for session
    feedback_form = FeedbackForm()
    if feedback_form.validate_on_submit():
        for dictionary in form_content:
            if data['project_category'] == dictionary['category']:
                feedback_lst = {
                    'question_1' : feedback_form.question_1.data,
                    'question_2' : feedback_form.question_2.data,
                    'question_3' : feedback_form.question_3.data
                } # make this a dict somewhere else

                for i in range(1, 4):
                    body += f'Question {i}\n'
                    body += dictionary[f'question {i}'] + '\n'
                    body += 'Rating: ' + feedback_lst[f'question_{i}'] + '\n\n' # don't leave blank on last

        subject = f"Feedback from {data['individual_name']}"
        SEND_EMAIL.send(subject, body)
        return render_template('thank_you.html')
    return render_template('form.html', feedback_form=feedback_form, form_content=form_content, data=data)