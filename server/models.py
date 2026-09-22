from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model):
    __tablename__ = "earthquakes"     # the table's name in the database

    id = db.Column(db.Integer, primary_key=True)    # Unique ID will be assigned automatically
    magnitude = db.Column(db.Float)                 # Float = decimal number
    location = db.Column(db.String)   
    year = db.Column(db.Integer)

    def to_dict(self):  # converts an Earthquake into a dictionary
        return {
            "id": self.id,
            "magnitude": self.magnitude,
            "location": self.location,
            "year": self.year,
        }

    def __repr__(self):     # controls how an Earthquake will print
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"