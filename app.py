from flask import Flask, request, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Nigel"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension

connect_db(app)

@app.route('/')
def show_pet_list():
    """Shows list of pets up for adoption"""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Shows form to add pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        if photo_url:
            new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        else:
            new_pet = Pet(name=name, species=species, age=age,notes=notes)

        db.session.add(new_pet)
        db.session.commit()        

        flash(f"{name} is added!", "alert alert-success")
        return redirect('/')

    else:
        return render_template('add-pet-form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_details(pet_id):
    """Shows details about pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.", "alert alert-success")
        return redirect('/')

    else:
        return render_template('edit-pet-form.html', pet=pet, form=form)



