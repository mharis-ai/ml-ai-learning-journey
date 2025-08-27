# Demonstrates inheritance and method overriding
# Shows how a child class can extend a parent class and override methods
class Battery:
    def battery_info(self):
        return "New Battery Installed"

class Engine:
    def engine_condition(self):
        return "Powerful"

class ElectricCar(Battery, Engine):
    pass

car = ElectricCar()
print(car.battery_info())
print(car.engine_condition())