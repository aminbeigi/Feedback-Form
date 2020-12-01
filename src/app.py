from flask import Flask, render_template
from forms import UserInfoForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '6ba6b74d871b12dea79bfc9013067c7c'

content = [
    {
        'title' : 'web development',
        'question' : 'Quality and value of user inferfaces.'
    },
    {
        'title' : 'security',
        'question' : 'Quality, value, and speed of secuiryt services.'
    }
]

@app.route('/')
@app.route('/home')
def home():
    user_form = UserInfoForm()
    return render_template('home.html', content=content, user_form=user_form)

@app.route('/home/form')
def form():
    return render_template('form.html', form=form, content=content)

if __name__ == '__main__':
    app.run(debug=True)