from models import Hero
def heroes():
    try:
        all_heroes = [hero.to_dict() for hero in Hero.query.all()]
        return all_heroes, 200
    except Exception as e:
            app.logger.error(f"Error in HeroesEndpoint: {str(e)}")
            return make_response({"error": "Serialization error"}, 500)

