
class Flight():
    counter = 1
    def __init__(self,origin,destination,duration):
        
        #keep track of every flight created
        self.id = Flight.counter
        Flight.counter += 1

        #keep track of passengers
        self.passengers = []
        
        #Details about Flight
        self.origin = origin
        self.destination = destination
        self.duration = duration


    def print_info(self):
        print("Flight Origin:{}".format(self.origin))
        print("Flight Destination:{}".format(self.destination))
        print("Flight Duration:{}".format(self.duration))


        print()

        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")



    def delay(self, amount):
        self.duration += amount


    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id





class Passenger():
    def __init__(self,name):
        self.name = name


def main():

    f1 = Flight(origin = "Paris", destination = "Berlin", duration = 340)
    f2 = Flight(origin = "Melbourne", destination = "Tokyo", duration = 350)

    alice = Passenger(name = "Alice")
    james = Passenger(name = "James")
    Wilfred = Passenger(name = "Wilfred")
    Motun = Passenger(name = "Motun")

    f1.add_passenger(alice)
    f1.add_passenger(james)

    f2.add_passenger(Wilfred)
    f2.add_passenger(Motun)


    # f1.print_info()
    # f2.delay(100)
    # f2.print_info()

print(Flight.counter)


if __name__ == "__main__":
    main()