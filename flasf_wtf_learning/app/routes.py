from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from flasf_wtf_learning.app import app, db, bcrypt
from flasf_wtf_learning.app.forms import LoginForm, RegistrationForm
from flasf_wtf_learning.app.models import User


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:  # current_user.is_authenticated is made to tell if we are already logged in or nit
        flash('You are already in the system, no need to registrate again', category='success')
        return redirect(url_for('home'))
    form = RegistrationForm()
    success = 'Looks good'
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password_reg.data).decode('utf-8')  # we hash our password
        user = User(username=form.username_reg.data, email=form.email_reg.data,
                    password=hashed_password)  # create new user in the db
        db.session.add(user)
        db.create_all()
        db.session.commit()

        flash('Your account has been created, you can now login', category='success')
        return redirect(url_for('login1'))

    return render_template('register.html', title='Register',
                           form=form)  # form=from means, that we are using the form=RegistrationForm as the template


@app.route('/login_reg', methods=['POST', 'GET'])
def login1():
    if current_user.is_authenticated:  # current_user.is_authenticated is made to tell if we are already logged in or nit
        flash('You are already in the system, no need to log in again', category='success')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # we are trying to find the same email in the db
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # when if there is the same email and dehashed password corresponds to the one, we typed in, then we will be logged in
            login_user(user, remember=form.remember.data)
            flash('You have been successfully logged in', category='success')
            next_page=request.args.get("next")

            return redirect(url_for(next_page)) if next_page else redirect(url_for('home'))

        else:
            flash("Login Unsuccessful. Please check your data ", category='danger')

    return render_template('login.html', title='Login',
                           form=form)  # form=from means, that we are using the form=LoginForm as the template


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('You are logged out', category='success')
    return redirect(url_for('home'))



@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
