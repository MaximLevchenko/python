from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'hello world man'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfpwzAaAAAAABEqfz8xJbWeZJSKPiJwh10kmU8W'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfpwzAaAAAAAGhiwF0pfFNPwHbmyZZJaMn2eqE5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.site.db'  # access to the SQL
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login1' #all info in the docs... When we are trying to access the page, which requires to be logged in, we will be redirected to login1 function
login_manager.login_message_category = 'info'
from flasf_wtf_learning.app import routes
