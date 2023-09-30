from models import Power

def powers():
    try:
        all_powers = [power.to_dict() for power in Power.query.all()]
        return all_powers, 200
    except Exception as e:
        app.logger.error(f"Error in PowersEndpoint: {str(e)}")
        return make_response({"error": "Serialization error"}, 500)