from flask import render_template, abort
from . import main
from ..models import User

@main.route('/')
def index():
    return render_template('main/index.html', session=False)

@main.route('/about')
def about():
    return render_template('main/about.html')

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(name=username).first()
    if not user:
        abort(404)
    return render_template('main/profile.html', user=user)