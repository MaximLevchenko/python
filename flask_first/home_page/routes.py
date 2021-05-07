from flask import render_template, url_for, flash, redirect, request, Blueprint, session


home_page=Blueprint('home_page',__name__, static_folder='static', template_folder='templates')


@home_page.route('/')
@home_page.route('/home')
def home():
    return render_template('index.html', title='Home page')