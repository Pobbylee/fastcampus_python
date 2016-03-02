# my car

class car:
    """
    This is car class
    """

    def __init__(self, car_name, car_color, car_cc):
        self.name = car_name
        self.color = car_color
        self.cc = car_cc
        self.lifecycle = 3
        print "__init__ has done"

    def print_info(self):
        print "The name of this car is", self.name
        print "The color of this car is", self.color
        print "cc is", self.cc

    def go_straight(self):
        print "go straight!"
        self.lifecycle -= 1

        if self.lifecycle == 0:
            self.broken()

    def broken(self):
        print "This is broken"
        exit()

my_car = car("BMW", "black", 10000)
my_car2 = car("Lexus", "red", 100)
for x in range(0, 3):
    my_car.go_straight()
