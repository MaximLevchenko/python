from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = 'hello world'
    app.permanent_session_lifetime = timedelta(minutes=5)  # setting the time for long-lasting session
    with app.app_context():
        from flask_first.login_user.routes import login_user
        from flask_first.logout_user.routes import logout_user
        from flask_first.home_page.routes import home_page
        db.init_app(app)

        app.register_blueprint(login_user, url_prefix='/login')
        app.register_blueprint(logout_user, url_prefix='/logout')
        app.register_blueprint(home_page, url_prefix='')

    return app
