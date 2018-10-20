from flask_wtf import Form
from wtforms import StringField, IntegerField, validators, ValidationError
from application.games.models import Game, check_game_name

# Validator for checking if game exists in database
def check_game_exists(form, field):
    message = 'Tämän nimistä peliä ei löytynyt. Tarkista nimi tai lisää peli sivustolle'

    name = field.data
    if check_game_name(name) == False:
        raise ValidationError(message)


class ItemForm(Form):
    name = StringField('Myyntikohteen nimi', [validators.DataRequired(message = 'Nimi ei saa olla tyhjä')])
    price = IntegerField('Hinta', [validators.DataRequired()])
    description = StringField('Kohteen kuvaus')
    gameName = StringField('Pelin nimi', 
                           [validators.DataRequired(message = 'Nimi ei saa olla tyhjä'),
                           check_game_exists])

    class Meta:
        csrf = False



# Separate form for adding games to the sale item
class GameToItemForm(Form):
    name = StringField('Nimi', [validators.DataRequired(message = 'Nimi ei saa olla tyhjä'), check_game_exists])

    class Meta:
        csrf = False
