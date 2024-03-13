# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def compute_area(self):
    return self.length * self.width

my_rectangle = Rectangle(5, 4)
area = my_rectangle.compute_area()
print("Area of the rectangle:", area) 