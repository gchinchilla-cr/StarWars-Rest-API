from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    birth = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    skin_color= db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
        }

class Planets(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    fav_planets = db.relationship("Planets")
    fav_people = db.relationship("People")
    fav_user = db.relationship("User")

    def __repr__(self):
        return '<Favorites %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planets_id": self.planets_id,
        }



    