from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError

from application.auth.models import check_username

# Validator for username field
def check_username_already_exists(form, field):
    message = 'Tämän niminen käyttäjätunnus on jo olemassa'

    name = field.data
    if check_username(name) == True:
        raise ValidationError(message)


class LoginForm(FlaskForm):
    username = StringField('Käyttäjä')
    password = PasswordField('Salasana')

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField('Käyttäjä',
                           [validators.DataRequired(message = 'Käyttäjänimi ei saa olla tyhjä'),
                            validators.Length(min = 1, max = 15, message = 'Käyttäjätunnuksen on oltava 1-15 merkkiä pitkä'),
                            check_username_already_exists]
                            )
    password = PasswordField('Salasana',
                            [validators.DataRequired(message = 'Salasana ei saa olla tyhjä'),
                            validators.Length(min = 5, max = 25, message = 'Salasanan on oltava 5-25 merkkiä pitkä')]
                            )
    email = StringField('Sähköposti',
                        [validators.Email(message = 'Sähköposti ei hyväksytyssä muodossa')]
                        )
    location = StringField('Sijainti',
                           [validators.DataRequired(message = 'Sijainti ei saa olla tyhjä'),
                            validators.Length(min = 1, max = 15, message = 'Sijainnin on oltava 1-15 merkkiä pitkä')]
                            )
  
    class Meta:
        csrf = False