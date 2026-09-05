
#class and object

class Car:
    total_car = 0 # since the variable it declare immdeate after class def it wil count also +1 whenever function is called ...therefore we will acces it with the __init__ function Car.total_car
    def __init__(self, brand, model):
        self.__brand = brand # double undersore __ make a attributes private .. will able to acces within class... calling it in object is not allowed (Encapsulation)
        self.__model = model
        self.total_car +=1

    def get_brand(self):
        return self.__brand

    #functionality to call full name
    def full_name(self):
        return f"{self.__brand}  {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod #decorator
    def general_discription():
        return "Car are the means of transportation"

    @property  # decorator
    def model(self):
        return self.__model

#creating an electricCar calss that inherits from the Car and has an addtional attrubute battrey_size
    
class ElectricCar(Car):
    def __init__(self,brand, model, Battery_size):
        super().__init__(brand,model)   #super() - specical syntax to recall the above class __init__ function name (attributes)
        self.Battery_size = Battery_size

    def Efull_name(self):
        return f"{self.brand} {self.model} {self.Battery_size}" 

    def fuel_type(self):
            return "Electric charge"   

my_tesla = ElectricCar("tesla","model-y", "76khw")

# isinstance((my_tesla, Car))
# isinstance((my_tesla, ElectricCar))


# my_car = Car("mercedes","s-class")
# print(my_tesla.model)
# print(my_tesla.Efull_name())
        

# my_car = Car("bmw", "520i")  
# print(my_car.full_name())
# print(my_tesla.fuel_type()) 
# print(my_car.fuel_type())

# print(my_car.general_discription())
# print(Car.general_discription())
# # my_car.model ="city"
# print(my_car.model)


class Battery: # inheritance multiple class 
    def batter_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo (Battery, Engine, Car):
    pass    

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.batter_info())