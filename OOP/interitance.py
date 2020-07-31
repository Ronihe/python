import test
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.__model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.__model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printDetails(self):
        self._Vehicle__model = "Roni"
        super().printDetails()

        print("Doors:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printDetails()


class Vehicle1:  # defining the parent class
    fuelCap = 90


class Car1(Vehicle1):  # defining the child class
    fuelCap = 50

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap)

        # accessing fuelCap from the Vehicle class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car1()  # creating a car object
obj1.display()  # calling the Car class method display()
test.test()