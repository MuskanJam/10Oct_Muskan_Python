#  Write a Python program to calculate the area of a trapezoid.

base1=int(input("Enter the first base of trapezoid:"))
base2=int(input("Enter the second base of trapezoid:"))

height = int(input("Enter a the height of trapezoid:"))

area = 0.5 * (base1 + base2) * height
print("The area of trapezoid", area)