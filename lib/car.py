from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_number, wheel_size):
        super().__init__(wheel_number, wheel_size)
        self.horsepower = 400

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

