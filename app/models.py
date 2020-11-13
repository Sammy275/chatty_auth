from werkzeug.security import generate_password_hash, check_password_hash
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
    # role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    @property
    def password(self):
        raise AttributeError("Password is not a readable field")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def loaduser(user_id):
    return User.query.get(int(user_id))