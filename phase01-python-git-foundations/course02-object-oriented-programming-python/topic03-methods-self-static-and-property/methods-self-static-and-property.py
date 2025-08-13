# Demonstrates method types in Python classes
# - Regular method (accessed via object)
# - Static method using @staticmethod decorator
# - Property method using @property decorator
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def fuel_type(self):
        return "Diesel"

    @staticmethod
    def general_description():
        return "Cars are comfortable"

    @property
    def mymodel(self):
        return self.__model

car3 = Car("Honda", "Civic")
print(car3.fuel_type())
print(Car.general_description())
print(car3.mymodel)