from models import Power, db
from flask import jsonify, make_response, request
def patch_power(id, app):
    try:

        power = Power.query.filter_by(id=id).first()

        if power:
            data = request.get_json()

            if 'description' in data:
                try:
                    description = data['description']
                    power.validate_description('description', description)
                except Exception as ve:
                    response_body = {"error":str(ve)}
                    return make_response(jsonify(response_body), 400)

            for key, value in data.items():
                setattr(power, key, value)

                db.session.add(power)
                db.session.commit()

                patched_power = {
                "id": power.id,
                "name": power.name,
                "description": power.description,
                }
                
                response = make_response(
                    jsonify(patched_power),
                    200
                )

            return response

        else:
            response_body = {"error":"Power Not Found"}
            return make_response(jsonify(response_body), 404)
    except Exception as e:
        app.logger.error(f"Error in PatchPower {str(e)}")
        return make_response({"error": "Serialization Error"}, 500)
