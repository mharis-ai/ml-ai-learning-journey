# Demonstrates basic class and object creation in Python
# Shows how to define a class, create an object, and access its methods
class Car:
    Total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.Total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"

car1 = Car("Nissan", "Patrol")
print(f"My First Car is [{car1.full_name()}]")