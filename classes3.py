class Flight():
    def __init__(self,origin,destination,duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


    def print_info(self):
        print("Flight Origin:{}".format(self.origin))
        print("Flight Destination:{}".format(self.destination))
        print("Flight Duration:{}".format(self.duration))

    def delay(self,amount):
        self.duration += amount

def main():

    f1 = Flight(origin = "New York", destination = "Toronto", duration = 240)
    f1.delay(20)
    f1.print_info()


if __name__ == "__main__":
    main()