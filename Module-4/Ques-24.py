# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def compute_area(self):
    return math.pi * self.radius ** 2

  def compute_perimeter(self):
    return 2 * math.pi * self.radius
  
my_circle = Circle(5)
print("Area of the circle:", my_circle.compute_area())  
print("Perimeter of the circle:", my_circle.compute_perimeter()) 