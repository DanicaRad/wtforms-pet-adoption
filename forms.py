from typing import Any
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding pets to adoption db."""

    name = StringField("Pet's name", validators=[InputRequired()])

    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    photo_url = StringField("Pet Photo URL", validators=[URL(), Optional(), URL()])

    age = IntegerField("Pet's Age", validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField("Additional notes about this pet", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit existing pet"""

    photo_url = StringField("Pet photo URL", validators=[URL(), Optional(), URL()])

    notes = TextAreaField("Additional notes about this pet", validators=[Optional()])

    available = BooleanField("Available?")