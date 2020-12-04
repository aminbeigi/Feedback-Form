from flask import Flask
from feedbackform.static_config_parser import StaticConfigParser

config = StaticConfigParser()

app = Flask(__name__)
app.config['SECRET_KEY'] = config.get('KEY', 'secret_key')

from feedbackform import routes