from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_first.admin.second import second
from flask_first.login_user.login import login

# basic Flask app setup
app = Flask(__name__)
app.secret_key = 'hello world'
app.register_blueprint(second, url_prefix='/test')
app.register_blueprint(login, url_prefix='login_user')
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


# login_user page



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
    elif 'user' and 'password' not in session:  # if we are not logged, redirect to the login_user page
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

    return redirect(url_for('login'))  # when we popped out the session, we come back to the login_user page


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
