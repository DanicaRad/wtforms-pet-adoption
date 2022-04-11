from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# default_photo = "https://ibb.co/vQYBDcs"

class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"<id={p.id} name={p.name} species={p.species} photo_url={p.photo_url} age={p.age} notes={p.notes} available={p.available}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)
