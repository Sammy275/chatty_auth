from flask import render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_required, login_user, current_user
from . import auth
from app.auth.forms import RegisterForm, LoginForm
from ..models import User
from app import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Please log out to log-in to a new account")
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('You have been logged in')
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid Username or Password')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.name.data, password=form.password.data, user_age=form.year.data)
        db.session.add(user)
        db.session.commit()
        flash("You are registered. Now you can log in to your account")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('main.index'))
