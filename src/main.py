"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favorites


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def getUser():

    usuario = User.query.all()
    request = list(map(lambda usuario:usuario.serialize(),usuario))    
    return jsonify(request), 200

# Endpoint people
@app.route('/people', methods=['GET'])
def getPeople():
    persona = People.query.all()
    request = list(map(lambda persona:persona.serialize(),persona))    
    return jsonify(request), 200

# Endpoint planets
@app.route('/planets', methods=['GET'])
def getPlanets():
    planeta = Planets.query.all()
    request = list(map(lambda planeta:planeta.serialize(),planeta))    
    return jsonify(request), 200

# Endpoint favorites
@app.route('/favorites', methods=['GET'])
def getFavorites():
       favorito = Favorites.query.all()
       request = list(map(lambda favorito:favorito.serialize(),favorito))
       return jsonify(request), 200

@app.route('/favorites', methods=['POST'])
def postFavorites():
        favorito = Favorites()
        favorito.planets_id = request.json['planets_id']
        favorito.people_id = request.json['people_id']
        favorito.user_id = request.json['user_id']
        db.session.add(favorito)
        db.session.commit()
        return jsonify({"mensaje": "Favorite successfully add"}), 200


@app.route('/favorites/<id>', methods=['DELETE'])
def delete(id):
    favorito = Favorites.query.get(id)
    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"mensaje": "Favorite successfully deleted"}), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
