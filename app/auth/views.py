from flask import render_template
from . import auth
from app.auth.forms import RegisterForm

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register')
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)