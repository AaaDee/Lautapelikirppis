from flask_wtf import Form
from wtforms import StringField, IntegerField, validators, ValidationError

from application.games.models import check_game_name

def check_game_already_in_db(form, field):
    message = 'Tämän niminen peli löytyy jo sivustolta'

    name = field.data
    if check_game_name(name) == True:
        raise ValidationError(message)


class GameForm(Form):
    name = StringField('Nimi',
                       [validators.DataRequired(message = 'Nimi ei saa olla tyhjä'),
                       validators.Length(max = 30, message = 'Enimmäispituus 30 merkkiä'),
                       check_game_already_in_db]
                       )
    bgg = IntegerField('BGG-tunnus', [validators.Optional(),
                       validators.NumberRange(min = 1, max = 9999999, message = 'Tunnuksen on oltava välillä 1-9999999 tai tyhjä')]
                       )
    


    class Meta:
        csrf = False