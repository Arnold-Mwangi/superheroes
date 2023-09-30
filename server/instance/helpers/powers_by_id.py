from models import Power
from flask import make_response, jsonify

def powers_by_id(id, app):
    try:
        power = Power.query.filter_by(id=id).first()
        
        if power:
            power_data = power.to_dict()
            return make_response(power_data, 200)
        else:
            response_body = {"error":"Power Not Found"}
            return make_response(jsonify(response_body), 404)
    except Exception as e:
        app.logger.error(f"Error in PowerById: {str(e)}")
        return({"error": "Serialization Error"}, 500)