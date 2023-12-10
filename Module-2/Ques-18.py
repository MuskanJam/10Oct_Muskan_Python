# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add'ly' instead if the string length of the given string is less than 3, leave it unchanged.
def my_str(str):
  
  if len(str) < 3:
    print(str)
  elif str.endswith('ing'):
    print(str + 'ly')
  else:
    print(str + 'ing')

a = input("Enter a string:")

result = my_str(a)