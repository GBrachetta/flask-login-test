from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = "You cannot access this page. Please log in."
login.login_message_category = 'info'
app.config['MONGO_URI'] = Config.MONGO_URI
mongo = PyMongo(app)

from app import routes, users