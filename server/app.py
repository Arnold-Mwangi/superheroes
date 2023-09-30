#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from instance.helpers import heroes, heroes_by_id, powers, patch_power_by_id, powers_by_id, post_hero_power

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/')
def home():
    response_body = {
        "Message": "Welcome to the world of heroes"
    }
    return make_response(jsonify(response_body), 200)

# GET /heroes
class HeroesEndpoint(Resource):    
    def get(self):
        all_heroes, status_code = heroes.heroes()
        return make_response(all_heroes, status_code)
        

# GET /heroes/:id
class HeroesById(Resource):
    def get(self, id):
        hero_response = heroes_by_id.heroes_by_id(id, app)
        return hero_response

class PowersEndpoint(Resource):
    def get(self):
        all_powers, status_code = powers.powers()
        return make_response(all_powers, status_code)


class PowersById(Resource):
    def get(self, id):
        hero_response = powers_by_id.powers_by_id(id, app)
        return hero_response

    def patch(self, id):
        patch_response = patch_power_by_id.patch_power(id, app)
        return patch_response


class HeroPowersEndPoint(Resource):
    def post(self):
        post_response = post_hero.post_hero_power(app)
        return post_response

api.add_resource(HeroPowersEndPoint, '/heropower')
api.add_resource(HeroesEndpoint, '/heroes')
api.add_resource(HeroesById, '/heroes/<int:id>')
api.add_resource(PowersEndpoint, '/powers')
api.add_resource(PowersById, '/powers/<int:id>')

if __name__ == '__main__':
    app.run(port=5555)
