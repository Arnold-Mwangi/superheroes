from models import HeroPower, Hero, Power, db
from flask import make_response, jsonify, request

def post_hero_power(app):
    try:
        data = request.json

        if 'strength' in data:
            try:
                strength = data['strength']
                HeroPower.validate_strength(None, 'strength', strength)
            except Exception as ve:
                response_body = {"error": str(ve)}
                return make_response(jsonify(response_body), 400)

        hero = Hero.query.get(data.get('hero_id'))
        power = Power.query.get(data.get('power_id'))

        if not hero:
            response_body = {"error": "Hero with specified ID not found"}
            return make_response(jsonify(response_body), 404)

        if not power:
            response_body = {"error": "Power with the specified ID not found"}
            return make_response(jsonify(response_body), 404)

        new_hero_power = HeroPower(
            strength=data.get('strength'),
            hero_id=data.get('hero_id'),
            power_id=data.get('power_id')
        )

        db.session.add(new_hero_power)
        db.session.commit()

        created_heroPower = HeroPower.query.get(new_hero_power.id)
        response_body = {"message": "HeroPower created successfully", "data": created_heroPower.to_dict()}
        return make_response(jsonify(response_body), 201)

    except Exception as e:
        app.logger.error(f"Error in post_hero_power: {str(e)}")
        response_body = {"error": "Serialization Error"}
        return make_response(jsonify(response_body), 500)
