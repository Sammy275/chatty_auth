from flask import render_template, request, flash
from . import auth
from app.auth.forms import RegisterForm

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():  
        return "nice"
    return render_template('auth/register.html', form=form)