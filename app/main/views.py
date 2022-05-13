from app import db
from app.models import User, Pitch
from . import main
from flask import render_template

@main.route('/')
def index():
  title = 'Welcome to Pitch App'
  pitches = Pitch.query.all()
  
  return render_template('index.html', title = title, pitches = pitches)
