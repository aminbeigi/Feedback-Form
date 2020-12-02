from flask import Flask, render_template, url_for, redirect, session, request
from forms import UserInfoForm, FeedbackForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '6ba6b74d871b12dea79bfc9013067c7c'

form_content = [
    {
        'title' : 'web development',
        'question 1' : 'Quality and value of user inferfaces.',
        'question 2' : 'Features have been added as requested (i.e. buttons).',
        'question 3' : 'Do you want an extended meeting about ideas on how to firther grow your business?'
    },
    {
        'title' : 'security',
        'question' : 'Quality, value, and speed of secuiryt services.',
        'question 2' : '',
        'question 3' : 'Do you want an extended meeting about ideas on how to firther grow your business?'
    }
]

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    user_form = UserInfoForm()
    if user_form.validate_on_submit():
        data = {
            'name' : user_form.project_name.data,
            'project_name' : user_form.project_name.data,
            'project_category' : user_form.project_category_name.data
        }
        session['data'] = data #session (cookie) variable
        return redirect(url_for('form', data=data))
    return render_template('home.html', user_form=user_form, form_content=form_content)

@app.route('/home/form')
def form():
    data = request.args['data']  # counterpart for url_for()
    data = session['data']       # counterpart for session
    feedback_form = FeedbackForm()
    return render_template('form.html', feedback_form=feedback_form, form_content=form_content, data=data)

if __name__ == '__main__':
    app.run(debug=True)