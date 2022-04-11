"""Seed file to make sample db"""

from models import Pet, db
from app import app

# Create all tables

db.drop_all()
db.create_all()

pets = [
    Pet(name="Winnie", species="dog", age=8, available=True),
    Pet(name="Nigel", species="dog", age=7, available=True), 
    Pet(name="Charlie", species="cat", age=5, available=True),
    Pet(name="Perry", species="porcupine", age=2, available=True)
]

db.session.add_all(pets)
db.session.commit()