from app import db
from app.models import User, Pitch
from . import main
from flask import render_template

from flask import render_template, redirect, url_for, flash, request
from . import main
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db
from flask_login import login_user, login_required, logout_user


@main.route('/')
def index():
  title = 'Welcome to Pitch App'
  #pitches = Pitch.query.all()
  
  return render_template('index.html', title = title)

@main.route('/login', methods=['GET', 'POST'])
def login():
  title = 'Pitch App || Log In'
  login_form = LoginForm()
  if  login_form.validate_on_submit():
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user, login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password')

  return render_template('auth/login.html', login_form = login_form, title = title)

@main.route('/signup', methods = ['GET', 'POST'])
def register():
  title = 'Pitch App || Create Account'
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username = form.username.data, email = form.email.data, password = form.password.data)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.login'))

  return render_template('auth/signup.html', registration_form = form, title = title)

@main.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))