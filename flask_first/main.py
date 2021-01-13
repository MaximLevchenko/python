from datetime import timedelta

from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hello world'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)  # setting the time for long-lasting session
db = SQLAlchemy(app)


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


@app.route('/')
def home():
    return render_template('index.html')


# login page methods refer to the kind of access we get
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':  # checking if the method is POST, it means that all went properly
        if request.form['nm'] == 'admin' or request.form['ps'] == 'secret':
            flash("You were successfully logged in into the admin's user page")
            session.permanent = True
            session['user'] = request.form['nm']
            password = request.form['ps']
            return redirect(url_for('administrating'))
        else:
            flash(f"You were successfully logged in", category='success')
            session.permanent = True  # setting the bool of session to permanent
            session['user'] = request.form['nm']  # requesting the name of user loggeg
            password1 = request.form['ps']
            user1 = session['user']  # user1 not a function
            found_user = users.query.filter_by(name=user1).first()
            if found_user:
                session['email'] = found_user.email
                session['password'] = found_user.password  # from the class
            else:
                usr = users(user1, '', password1)
                db.session.add(usr)
                db.session.commit()
            return redirect(
                url_for('user'))  # redirecting to the user's page after logging in(using user's name)
    else:
        if 'user' in session:  # if user is already logged, it will download the user page.
            flash('You are already logged in, to log out, type logout')
            return redirect(url_for('user'))
        elif 'user' not in session:
            flash("You have not logged yet", category='success')
            return render_template('login.html', error=error)  # if it didn't go properly, we force the comeback
            # to the login page again


@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if 'user' in session:  # if we logged, redirect the user page
        user2 = session['user']
        if request.method == "POST":
            email1 = request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name=user2).first()
            found_user.email = email1
            db.session.commit()
            flash(f"Here is your email: {email1}")
        else:
            if 'email' in session:
                email = session['email']
        return render_template('user.html', email=email)
    else:  # if we are not logged, redirect to the login page
        return redirect(url_for('login'))


@app.route('/admin')
def administrating():
    if 'user' in session:
        return render_template('admin.html')


@app.route('/view')
def view():
    if 'user' in session:
        return render_template('view.html', values=users.query.all())
    else:
        flash('You are not logged in to see this information', category='info')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'user' in session:
        user3 = session['user']
        flash(f'Logged out successfully, {user3}', category='info')
    session.pop('user', None)  # just pops out the session
    session.pop('email', None)

    return redirect(url_for('login'))  # when we popped out the session, we come back to the login page


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
# @app.route('/<name>')
# def user(name):
#   return f'Hello {name}'


'''
@app.route('/admin')
def admin():
    return redirect(url_for('user', name='Admin!!'))  #when we try to access admin, it just redirects to the page we want
                                      # (in brackets we use the name of the function)
'''
