#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

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
        try:

            all_heroes = [hero.to_dict() for hero in Hero.query.all()]
            return make_response(all_heroes, 200)
        except Exception as e:
            app.logger.error(f"Error in HeroesEndpoint: {str(e)}")
            return make_response({"error": "Serialization error"}, 500)

# GET /heroes/:id
class HeroesById(Resource):

    def get(self, id):
        try:
            hero = Hero.query.filter_by(id=id).first()
            if hero:
                hero_data = hero.to_dict()
                return make_response(hero, 200)
            else:
                response_body = {"Error": "Power Id not Available"}
                return make_response(response_body, 500)
        except Exception as e:
            app.logger.error(f"Error in HeroesBYiD: {str(e)}")
            return make_response({"error":"Serialization Error"}, 500)

api.add_resource(HeroesEndpoint, '/heroes')
api.add_resource(HeroesById, '/heroes/<int:id>')

if __name__ == '__main__':
    app.run(port=5555)
