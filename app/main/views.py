from app import db
from app.models import User
from . import main
from flask import render_template

@main.route('/')
def index():
  title = 'Welcome to Pitch App'
  return render_template('index.html',title=title)
