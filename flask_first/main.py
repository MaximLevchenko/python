from datetime import timedelta

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = 'hello world'
app.permanent_session_lifetime = timedelta(minutes=5) #setting the time for long-lasting session


@app.route('/')
def home():
    return render_template('index.html')


# login page          methods refer to the kind of access we get
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # checking if the method is POST, it means that all went properly
        session.permanent = True  #setting the bool of session to permanent
        user = request.form['nm']  # requesting the name of user loggeg
        session['user'] = user

        return redirect(
            url_for('user'))  # redirecting to the user's page after logging in(using user's name)
    else:
        if 'user' in session: # if user is already logged, it will download the user page.
            return redirect(url_for('user'))
        return render_template('login.html')  # if it didn't go properly, we force the comeback to the login page again


@app.route('/user')
def user():
    if 'user' in session:# if we logged, redirect the user page
        return render_template('user.html')
    else: # if we are not logged, redirect to the login page
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None) #just pops out the session
    return redirect(url_for('login'))#when we popped out the session, we com


if __name__ == '__main__':
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
