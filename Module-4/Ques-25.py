# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass) to inherit attributes and methods from an existing class (superclass). 

class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
  def speak(self):
    return f"{self.name} says woof!"


class Cat(Animal):
  def speak(self):
    return f"{self.name} says meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  
print(cat.speak())  

# We define a superclass Animal with an __init__ method (constructor) and a speak method.
# A constructor is a special method within a class that is automatically called when a new instance (object) of the class is created. Constructors are used to initialize the object's attributes or perform any setup required for the object to function correctly.