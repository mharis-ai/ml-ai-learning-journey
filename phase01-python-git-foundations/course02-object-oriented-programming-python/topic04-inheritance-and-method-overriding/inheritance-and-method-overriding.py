# Demonstrates inheritance and method overriding
# Shows how a child class can extend a parent class and override methods
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def fuel_type(self):
        return "Diesel"
    
    def get_brand(self):
        return(self.__brand) 

    def get_model(self):
        return(self.__model) 
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Fully Electric"

car4 = ElectricCar("Tesla", "S", "100Kwh")
print(f"My Electric Car is [{car4.get_brand()} {car4.get_model()}] having {car4.fuel_type()} engine")