from flask import render_template, url_for, flash, redirect, request, Blueprint, session

logout_user = Blueprint('logout_user',__name__, static_folder='static', template_folder='templates')

@logout_user.route('/logout')
def logout():
    if 'user' in session:
        user3 = session['user']
        flash(f'Logged out successfully, {user3}', category='info')
    session.pop('user', None)  # just pops out the session
    session.pop('email', None)

    return redirect(url_for('login_user.login'))  # when we popped out the session, we come back to the login page
