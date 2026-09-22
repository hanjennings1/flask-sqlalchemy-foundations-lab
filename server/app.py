# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# GET EARTHQUAKE BY ID ---
@app.route('/earthquakes/<int:id>')  
def earthquake_by_id(id):
    quake = Earthquake.query.filter(Earthquake.id == id).first()

    if quake:
        body = quake.to_dict()
        status = 200
    else:
        # error handling / error message:
        body = {"message": f"Earthquake {id} not found."}
        status = 404

    return make_response(body, status)


# GET EARTHQUAKES MATCHING A MIN MAGNITUDE VALUE ---
@app.route('/earthquakes/magnitude/<float:magnitude>')  # <float:...> needs a decimal in the URL
def earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    body = {
        "count": len(quakes),                               # displays number of matches
        "quakes": [quake.to_dict() for quake in quakes],    # shows each match as a dictionary with its info
    }

    return make_response(body, 200) # always returns 200 -- even if none match, the request still works, just returns none



if __name__ == '__main__':
    app.run(port=5555, debug=True)
