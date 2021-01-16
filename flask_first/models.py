from flask import current_app
from flask_first import db



current_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3.db'  # access to the SQL
current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class users(db.Model):
    __tablename__ = 'users'
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password