from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Enter your username:', validators=[
                           DataRequired('Username is required')])
    email = StringField('Enter email address:', validators=[
                        DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired(), EqualTo(
        'password_confirm', message='Passwords must match')])
    password_confirm = PasswordField(
        'Confirm password:', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('An account with this email exists')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Username exists')


class LoginForm(FlaskForm):
    email = StringField('Enter your email address:',validators=[DataRequired(), Email()])
    password = PasswordField('Your password:', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')


class UpdateProfile(FlaskForm):
    username = StringField('Enter new username', validators=[DataRequired()])
    bio = TextAreaField('Enter bio', validators=[DataRequired()])
    submit = SubmitField('Update')


class PitchForm(FlaskForm):
    title = StringField('Pitch title:', validators=[DataRequired()])
    category = SelectField('Category:', choices=[('Technology'), ('Innovation')], validators=[DataRequired()])
    pitch = TextAreaField('Your Pitch:', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    comment = TextAreaField('Your Comment:', validators=[DataRequired()])
    submit = SubmitField('Post')
