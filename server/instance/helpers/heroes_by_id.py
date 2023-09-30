from models import Hero
from flask import make_response

def heroes_by_id(id, app):
    try:
        hero = Hero.query.filter_by(id=id).first()
        if hero:
            hero_data = hero.to_dict()
            return make_response(hero_data, 200)
        else:
            response_body = {"Error": "Power Id not Available"}
            return make_response(response_body, 500)
    except Exception as e:
            app.logger.error(f"Error in HeroesBYiD: {str(e)}")
            return make_response({"error":"Serialization Error"}, 500)