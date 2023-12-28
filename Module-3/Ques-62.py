# Write a Python program to calculate surface volume and area of a cylinder.

pi = 3.14
height = int(input("Enter height:"))
radian = int(input("Enter radian:"))
volume = pi * radian * radian * height
surface = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume is:", volume)
print("Surface area is:", surface)