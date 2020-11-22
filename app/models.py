from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
import datetime
from flask_login import UserMixin


from . import login_manager

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    register_date = db.Column(db.Date, default=datetime.date.today())
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    # role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


    # Password setting
    @property
    def password(self):
        raise AttributeError("Password is not a readable field")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    # Age setting
    @property
    def user_age(self):
        return self.age
    
    @user_age.setter
    def user_age(self, year):
        curr_date = str(datetime.date.today()).split('-')
        self.age = int(curr_date[0]) - int(year)

    # user account confirmation
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True


@login_manager.user_loader
def loaduser(user_id):
    return User.query.get(int(user_id))