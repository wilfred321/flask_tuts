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
    