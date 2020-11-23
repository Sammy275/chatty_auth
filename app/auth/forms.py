from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import Length, Email, DataRequired, Regexp, EqualTo
from wtforms.fields.html5 import EmailField
import datetime
from ..models import User
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0, "Username must have only letters, numbers, dots or underscores")])
    email = EmailField("Email", validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm_pass', message='Password must match')])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired()])
    day = SelectField("Day", choices=[(i, i) for i in range(1, 32)])
    month = SelectField("Month", choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')])
    year = SelectField("Year", choices=[(i, i) for i in range(1900, datetime.date.today().year + 1)])
    submit = SubmitField("Sign Up")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already registered.')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('The username is taken')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Keep me Logged In')
    submit = SubmitField("Log in")


class PasswordUpdateForm(FlaskForm):
    old_password = PasswordField("Password", validators=[DataRequired()])
    new_password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm_pass', message='Password must match')])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Save New Password")