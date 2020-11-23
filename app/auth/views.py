from flask import render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_required, login_user, current_user
from . import auth
from app.auth.forms import RegisterForm, LoginForm, PasswordUpdateForm, ForgotPasswordEmailForm, ForgotPasswordChangeForm
from ..models import User
from app import db
from ..emails import send_email

@auth.before_app_request
def before_request():
    if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != 'auth.':
        return redirect(url_for('auth.unconfirmed'))


###################### User Authentication ##########################################
# Login route

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If a user, who has already logged in, tries to acces the route
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

# Registration route

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.name.data, password=form.password.data, user_age=form.year.data)
        db.session.add(user)
        db.session.commit()
        
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)

        flash("A confirmation email has been sent to your email. Please check it")
        return redirect(url_for('main.index'))

    return render_template('auth/register.html', form=form)


# Route that will log out the user
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('main.index'))
#############################################################################################


##################### User account confirmations #################################
# User account confirmation route

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash("The confirmation link is invalid or has expired")
    return redirect(url_for('main.index'))

# If the user account is unconfirmed, this route will be executed

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

# Route to generate new confirmation token

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))
#########################################################################



####################### Account Management ############################### 
@auth.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    form = PasswordUpdateForm()
    if form.validate_on_submit():
        current_user.password = form.new_password.data
        db.session.add(current_user)
        db.session.commit()
        flash("Your password has been updated")
        return redirect(url_for('main.index'))
    return render_template('auth/update_password.html', form=form)

@auth.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    # If user is logged in then take them to main page
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = ForgotPasswordEmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        token = user.generate_confirmation_token()
        send_email(form.email.data, 'Change Password', 'auth/email/change_password_email', user=user, token=token)
        flash("A reset link has been sent to your email account")
        return redirect(url_for('auth.login'))
    return render_template('auth/forgot_password.html', form=form)

@auth.route('/change_password/<email>/<token>', methods=['GET', 'POST'])
def change_password(email, token):
    form = ForgotPasswordChangeForm()
    user = User.query.filter_by(email=email).first()
        
    if form.validate_on_submit():
        user.password = form.new_password.data
        db.session.add(user)
        db.session.commit()
        flash("Password has been changed. You can now log in")
        return redirect(url_for('auth.login'))
    
    
    if user.confirm(token):
        return render_template('/auth/change_password.html', form=form, email=email, token=token)
    flash("Link is invalid or has expired")
    return redirect(url_for('auth.login'))


##########################################################################