# Write a Python program to check whether an element exists within a tuple.

tup = ("1", "4", "M", "u", "21", "s", "70")

n=input("Enter an element:")

if n in tup:
  print("Element exists")
else:
  print("Element does not exists.")