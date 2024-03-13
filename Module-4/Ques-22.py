# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class. 

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def display_info(self):
    print(f"This is a {self.year} {self.make} {self.model}.")

my_car = Car("Toyota", "Camry", 2022)
print(my_car.make)  
print(my_car.model) 
print(my_car.year)  
my_car.display_info() 