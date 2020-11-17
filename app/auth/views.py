from flask import render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_required
from . import auth
from app.auth.forms import RegisterForm
from ..models import User
from app import db

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.name.data, password=form.password.data, user_age=form.year.data)
        db.session.add(user)
        db.session.commit()
        flash("You are now registered")
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('main.index'))
