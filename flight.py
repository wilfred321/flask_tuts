class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["Andy", "Chucks","Matt"]
for person in people:
    if flight.open_seats():
        flight.add_passenger(person)
        print(f"The passenger with name {person} was added to the flight")
        print(f"The current flight capacity is {flight.open_seats()}")
    else:   
        print(f"No seats available for {person}")
print(f"The final flight capacity is {flight.open_seats()}")
    
