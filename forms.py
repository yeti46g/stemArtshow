from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,RadioField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	password2= PasswordField('Repeat Password',validators = [DataRequired(),EqualTo('password', message = 'Passwords mush match.')])
	submit = SubmitField('Register') 

class LoginForm(FlaskForm):
	"""User Log-in Form."""
	username = StringField('Username',validators=[DataRequired()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Log In')

class DestinationForm(FlaskForm):
    city = StringField('city')
    country = StringField('country')
    description = StringField('description')
    submit = SubmitField('Post')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
