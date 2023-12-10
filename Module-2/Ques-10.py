# Write a python program that will return true if the wto given integers values are equal or their sum or difference is 5.
a=int(input("Enter any value:"))
b=int(input("Enter any value:"))

if a==b or a-b==5 or a+b==5:
  print("True")
else:
  print("False")