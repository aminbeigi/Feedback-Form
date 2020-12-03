from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '6ba6b74d871b12dea79bfc9013067c7c'

from feedbackform import routes