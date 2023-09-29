from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk" : "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db =SQLAlchemy(metadata = metadata)

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String)
    strength = db.column(db.String)

# add any models you may need. 