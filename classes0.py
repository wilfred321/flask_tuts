class Flight():
    def __init__(self,origin,destination,duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


    def print_info(self):
        print("Flight Origin:{}".format(self.origin))
        print("Flight Destination:{}".format(self.destination))
        print("Flight Duration:{}".format(self.duration))

def main():

    f1 = Flight(origin = "New York", destination = "Toronto", duration = 240)

    f2 = Flight(origin = "Detroit", destination = "Washington", duration = 320)
    
    
    f1.print_info()

    f2.print_info()

if __name__ == "__main__":
    main()
