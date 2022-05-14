from app import db
from app.models import User, Pitch, Comment, Downvote, Upvote
from . import main
from flask import render_template

from flask import render_template, redirect, url_for, flash, request, abort
from . import main
from .forms import RegistrationForm, LoginForm, UpdateProfile, PitchForm, CommentForm
from ..models import User
from .. import db
from flask_login import login_user, login_required, logout_user, current_user


@main.route('/')
def index():
    title = 'Pitch App'
    pitches = Pitch.query.all()

    return render_template('index.html', title=title, pitches=pitches)


@main.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Pitch App || Log In'
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')

    return render_template('auth/login.html', login_form=login_form, title=title)


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    title = 'Pitch App || Create Account'
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('auth/signup.html', registration_form=form, title=title)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profiles/profile.html', user=user)


@main.route('/profile/<uname>/update', methods=['GET', 'POST'])
@login_required
def updateprofile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.username = form.username.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile', uname=user.username))

    return render_template('profiles/updateprofile.html', form=form)


@main.route('/create/pitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        pitch = form.pitch.data

        new_pitch_obj = Pitch(title=title, category=category,
                              pitch=pitch, user_id=current_user._get_current_object().id)
        new_pitch_obj.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('pitchform.html', form=form)


@main.route('/upvote/<int:id>', methods=['POST', 'GET'])
@login_required
def upvote(id):
    pitch_upvotes = Upvote.get_upvote(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch_v in pitch_upvotes:
        to_str = f'{pitch_v}'
        print(f'{valid_string} {to_str}')
        if valid_string == to_str:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_upvote = Upvote(user=current_user, pitch_id=id)
    new_upvote.save_upvote()

    return redirect(url_for('main.index', id=id))


@main.route('/downvote/<int:id>', methods=['POST', 'GET'])
@login_required
def downvote(id):
    pitch_downvotes = Downvote.get_downvote(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch_v in pitch_downvotes:
        to_str = f'{pitch_v}'
        print(f'{valid_string} {to_str}')
        if valid_string == to_str:
            return redirect(url_for('main.index', id=id))
        else:
            continue
    new_downvote = Downvote(user=current_user, pitch_id=id)
    new_downvote.save_downvote()

    return redirect(url_for('main.index', id=id))


@main.route('/new/comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def new_comment(pitch_id):
    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment_obj = Comment(
            comment=comment, pitch_id=pitch_id, user_id=current_user._get_current_object().id)

        new_comment_obj.save_comment()
        return redirect(url_for('main.new_comment', pitch_id=pitch_id))

    return render_template('commentform.html', form=form, comments=comments)
