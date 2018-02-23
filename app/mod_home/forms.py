from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CheckPassword(FlaskForm):
    password = StringField(
        'Lozinka',
        [
            DataRequired(message='Lozinka ne može biti prazna. Molim vas unesite lozinku.')
        ]
    )