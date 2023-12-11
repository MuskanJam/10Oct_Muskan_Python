# Write a Python function that checks whether a passed string is palindrome or not.

str = input("Enter a string:")

revstr = (str[::-1])

if revstr == str:
  print("Palindrome")
else:
  print("Not Palindrome")