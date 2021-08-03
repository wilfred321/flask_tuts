import os
from models import *
from flask import Flask, render_template,request
from flask import jsonify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)





@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html",flights=flights)



@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html",flights=flights)
    
@app.route("/book", methods = ["POST"])
def book():
    """Book a flight"""
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message = "Invalid flight number")

#Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message = "No such flight exists")

    #Add Passenger if the flight is not null

    # passenger = Passenger(name=name, flight_id=flight_id)
    # db.session.add(passenger)
    # db.session.commit()
    flight.add_passenger(name)
    return render_template("success.html")

    # passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    # return render_template('flight.html',flight=flight, passengers=passengers)


#Show the flight details page
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    try:
        flight = Flight.query.get(flight_id)
    except ValueError:
        return render_template("error.html", message = "No such flight exists" )
    
    #returns the passengers associated with a given flight
    #method 1
    # passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    #method 2
    passengers = flight.passengers
    return render_template ("flight.html",passengers=passengers,flight=flight)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):

    """Returns details about a single flight"""

     #make sure flight exists
    flight = Flight.query.get(flight_id)

    if flight is None:
        return jsonify({"error":"Invalid flight ID"}),422

#Get all passengers
    passengers = flight.passengers

    #Get all passengers.
    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
        "origin":flight.origin,
        "destination":flight.destination,
        "duration":flight.duration,
        "passengers":names

    })
