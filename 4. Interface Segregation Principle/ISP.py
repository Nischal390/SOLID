# A user should not depend on an interface or use an interface if they dont want to
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stoped")


class Boat(Vehicle):
    def start_engine(self):
        print("Boat engine started")

    def stop_engine(self):
        print("Boat engine stoped")

def test_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()

car = Car()
boat = Boat()

test_vehicle(car)
test_vehicle(boat)