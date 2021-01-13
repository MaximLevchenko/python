from datetime import timedelta

from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

# basic Flask app setup
app = Flask(__name__)
app.secret_key = 'hello world'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3.html'  # access to the SQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)  # setting the time for long-lasting session
db = SQLAlchemy(app)


# class, the table of the database
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


# home page
@app.route('/')
def home():
    return render_template('index.html')


# login page
@app.route('/login', methods=['POST', 'GET'])
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
            session['user'] = request.form['nm']  # we are just saying that the session['user']= the name, which we typed into the field
            user1 = session['user']  # user1 not a function
            session['password'] = request.form['ps']  # session['password']= field, in which we typed our password
            password1 = request.form['ps']

            found_user = users.query.filter_by(name=user1,
                                               password=password1).first()  # we are filtering all the users in the database by the name and password, we typed while logging in
            if found_user:  # if we have found this user, we say that the email he typed previously is now in the field of email
                session['email'] = found_user.email # we are saying that the email user typed previously, is now the session['email']
            else:
                usr = users(user1, '', password1)  # if we haven't found that user by name and password, we create a new one
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
            return render_template('login.html', error=error)  # if it didn't go properly, we force the comeback
            # to the login page again


@app.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if 'user' and 'password' in session:  # check, if the user with the correct password in session
        user2 = session['user']
        password1 = session['password']
        if request.method == "POST":  # if the user was not previously in the database, we want to add email for him
            email1 = request.form['email']
            found_user = users.query.filter_by(name=user2 , password=password1).first() # we find that user in the db with corresponding data and adding email to the db
            found_user.email = email1
            db.session.commit()
            flash(f"Here is your email: {email1}")
        else:
            if 'email' in session:
                email = session['email']
        return render_template('user.html', email=email)  # if it is, displays the email of that user typed earlier, which was saved in the db
    elif 'user' and 'password' not in session:  # if we are not logged, redirect to the login page
        return redirect(url_for('login'))

# page for admin
@app.route('/admin')
def administrating():
    if 'user' in session:
        return render_template('admin.html')

# database page
@app.route('/view')
def view():
    if 'user' in session:
        return render_template('view.html', values=users.query.all()) # returns the value of the whole database
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
#  TODO write a function, which deletes users in the database, you can use Tech With Tim video(8) as an example
