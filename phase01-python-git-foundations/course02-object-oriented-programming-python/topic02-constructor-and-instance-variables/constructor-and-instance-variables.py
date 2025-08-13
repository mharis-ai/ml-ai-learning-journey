# Demonstrates constructor (__init__) and instance variables
# Shows how to initialize objects with attributes and use getters
class Car:
    Total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand  # private instance variable
        self.__model = model
        Car.Total_car += 1

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

car2 = Car("Toyota", "Corolla")
print(f"My Second Car is [{car2.get_brand()} {car2.get_model()}]")