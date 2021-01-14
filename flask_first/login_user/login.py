from flask_first.main import *
from flask import Blueprint
from flask_first.main import users, db
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
login = Blueprint('login_user', __name__, static_folder='static', template_folder='templates')

@login.route('/')
def login():
    error = None
    if request.method == 'POST':  # checking if the method is POST, it means we got a query from button
        if request.form['nm'] == 'admin' or request.form['ps'] == 'secret':
            flash("You were successfully logged in into the admin's user page")
            session.permanent = True
            session['user'] = request.form['nm']
            password = request.form['ps']
            password = session['password']
            return redirect(url_for('administrating'))
        else:  # if we are not admins, continue with this code
            flash(f"You were successfully logged in", category='success')
            session.permanent = True  # setting the bool of session to permanent
            session['user'] = request.form[
                'nm']  # we are just saying that the session['user']= the name, which we typed into the field
            user1 = session['user']  # user1 not a function
            session['password'] = request.form['ps']  # session['password']= field, in which we typed our password
            password1 = request.form['ps']

            found_user = users.query.filter_by(name=user1,
                                               password=password1).first()  # we are filtering all the users in the database by the name and password, we typed while logging in
            if found_user:  # if we have found this user, we say that the email he typed previously is now in the field of email
                session[
                    'email'] = found_user.email  # we are saying that the email user typed previously, is now the session['email']
            else:
                usr = users(user1, '',
                            password1)  # if we haven't found that user by name and password, we create a new one
                db.session.add(usr)
                db.session.commit()
            return redirect(
                url_for('user'))  # redirecting to the user's page after logging in(using user's name)
    else:  # below is a standard script, which checks whether we are logged or not
        if 'user' in session:  # if user is already logged, it will download the user page.
            flash('You are already logged in, to log out, type logout')
            return redirect(url_for('user'))
        else:
            flash("You have not logged yet", category='success')
            return render_template('login_user.html', error=error)  # if it didn't go properly, we force the comeback
            # to the login_user page again

