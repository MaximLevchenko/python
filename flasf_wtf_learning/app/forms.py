from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo, InputRequired
from wtforms.validators import ValidationError
from flasf_wtf_learning.app.models import User


class RegistrationForm(FlaskForm):
    username_reg = StringField('Username', validators=[DataRequired(), InputRequired(), Length(min=2, max=20)])
    password_reg = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    password_reg_conf = PasswordField('Confirm password',
                                      validators=[DataRequired(), InputRequired(), Length(min=2, max=20),
                                                  EqualTo('password_reg',
                                                          message='Please make sure your passwords match')])  # EqualTo name should match the name of the variable we are comparing it to
    email_reg = StringField('Email', validators=[DataRequired(), InputRequired(), Email()])
    submit = SubmitField('Sign Up')

    def validate_username_reg(self, username_reg):
        user = User.query.filter_by(username=username_reg.data).first()#we try to find the similar one in the database, if it returns none, then user will be false and we`ll not go into the if clause
        if user:
            raise ValidationError('That username is taken, choose another one')
    def validate_email_reg(self, email_reg):
        user = User.query.filter_by(email=email_reg.data).first()
        if user:
            raise ValidationError('Account with this email already exists, choose another one')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), InputRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), InputRequired(), Length(min=2)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
