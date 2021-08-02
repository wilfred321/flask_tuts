
import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2


engine = create_engine(os.environ.get("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    file = open('flights2.csv')
    reader = csv.reader(file)

    for origin, destination, duration in reader:

        db.execute("INSERT INTO flights(origin,destination,duration) VALUES (:origin, :destination, :duration)",
                   {"origin": origin, "destination": destination, "duration": duration})
        print(
            f"Added flight from {origin} to {destination} lasting {duration} minutes")
    db.commit()


if __name__ == "__main__":
    main()
