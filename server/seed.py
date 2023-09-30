from random import choice
from models import Power, Hero, HeroPower, db
from app import app

if __name__ == '__main__':

    with app.app_context():
      db.session.query(HeroPower).delete()
      db.session.query(Hero).delete()
      db.session.query(Power).delete()
      db.session.commit()

      print("🦸‍♀️ Seeding powers...")
      powers_data = [
        { "name": "super strength", "description": "gives the wielder super-human strengths" },
        { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
        { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
        { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
      ]

      for info in powers_data:
        power = Power(**info)
        db.session.add(power)

      print( "🦸‍♀️ Seeding heroes...")
      heroes_data = [
        { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
        { "name": "Doreen Green", "super_name": "Squirrel Girl" },
        { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
        { "name": "Janet Van Dyne", "super_name": "The Wasp" },
        { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
        { "name": "Carol Danvers", "super_name": "Captain Marvel" },
        { "name": "Jean Grey", "super_name": "Dark Phoenix" },
        { "name": "Ororo Munroe", "super_name": "Storm" },
        { "name": "Kitty Pryde", "super_name": "Shadowcat" },
        { "name": "Elektra Natchios", "super_name": "Elektra" }
      ]

      for info in heroes_data:
        hero = Hero(**info)
        db.session.add(hero)

      print ("🦸‍♀️ Adding powers to heroes...")

      strengths = ["Strong", "Weak", "Average"]
      heroes = Hero.query.all()
      powers = Power.query.all()

      for hero in heroes:
        for info in range(choice([1, 2, 3])):
          power = choice(powers)
          strength = choice(strengths)

          hero_power = HeroPower(hero=hero, power=power, strength=strength)
          db.session.add(hero_power)
      
      db.session.commit()
      print ("🦸‍♀️ Done seeding!")
