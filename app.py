import os
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker,scoped_session

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
from flask import Flask,session,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template('index.html',flights = flights)


@app.route("/book", methods = ["POST"])

def book():
    """Book a flight."""
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message = "Invalid flight number")

    if db.execute("SELECT * FROM flights WHERE id = :id",{"id":flight_id}).rowcount== 0:
        return render_template("error.html",message = "No flight with such ID")
    
    db.execute("INSERT INTO passengers(name,flight_id)VALUES(:name, :flight_id)",{"name":name, "flight_id":flight_id})
    db.commit()
    return render_template("success.html")
    

#Display all the flights in the database
@app.route("/flights")
def flights():
    flights = db.execute("SELECT origin,destination,duration FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

#Return specific flights
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight"""
    flight = db.execute("SELECT * FROM flights WHERE id = :id",{"id":flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message = "No such flight exists!")
    
    #Get all passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
    {"flight_id":flight_id}).fetchall()
    return render_template("flight.html", flight=flight,passengers=passengers)



