
class Vehicle:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class VehicleOption:

    def radio(self):
        print("this vehicle has a RADIO")


class Car(Vehicle, VehicleOption):

    def __init__(self, name, color):
        super().__init__(name, color)


class Van(Car):

    def __init__(self, name, color):
        super().__init__(name, color)



class Boat(Vehicle):

    def __init__(self, name, color):
        super().__init__(name, color)


if __name__ == '__main__':


    c1 = Car("VW", "blue")



    v1 = Van("HYUNDAI", "green")


    b1 = Boat("my boat", "red")
