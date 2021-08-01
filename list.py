from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import scoped_session,sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin,destination,duration FROM flights")
    for flight in flights:
        print(f"{flight.origin} to {flight.destination},{flight.duration} minutes")

if __name__ == "__main__":
    main()



