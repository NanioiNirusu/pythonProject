# Object Oriented Programming
import abc

class IMovable(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass
class Vehicle(IMovable):
    def __init__(self): # constructor
        super().__init__()
        self._wheels = 0

    def move(self):
        print("move")
        
    def set_wheels(self, value):
        self._wheels = value

    def get_wheels(self):
        return self._wheels

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._wheels = 4
        self.brand = ""

    def drive(self, km):
        print(f"drive: {km}km")

car1 = Car() # car1 = newCar()
car1.set_wheels(8)
print(car1.get_wheels())
car1.brand = "BMW"
car2 = Car()
car2 = car1
car2.brand = "Mercedes"
print(car1.brand, car2.brand)

# car1.drive(10)
# print(car1)