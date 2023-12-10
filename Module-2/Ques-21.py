# Write a Python function to reverses a string if its length is a multiple of 4.
str = input("Enter a string:")
print(len(str))

if len(str) % 4 == 0:
  print("Its a reverse string.")
else:
  print("Not a reverse string.")