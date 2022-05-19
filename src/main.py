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
from models import db, User, People, PeopleFavorites, Planets, PlanetsFavorites
#from models import Person

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
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def people():
    people = People.query.all()

    response = []
    for p in people: 
        response.append(p.serialize())

    return jsonify(response)

@app.route('/planets', methods=['GET'])
def planets():
    planets = Planets.query.all()

    response =  []
    for p in planets:
        response.append(p.serialize())

    return jsonify(response)

    
# @app.route('/people/<int:people_id>', methods=['GET'])
# def get_people_id():
#      json_text = jsonify(people.results.id)
#      return json_text

# @app.route('/people', methods=['POST'])
# def add_people():
#     payload = request.get_json(force=True)
#     people.append(payload)
#     return jsonify(people)



# @app.route('/planets', methods=['POST'])
# def add_planets():
#     payload = request.get_json(force=True)
#     planets.append(payload)
#     return jsonify(planets)

# @app.route('/users', methods=['GET'])
# def get_users():
#      json_text = jsonify(users)
#      return json_text

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
