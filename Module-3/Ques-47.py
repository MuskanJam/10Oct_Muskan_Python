# Write a Python program to create a dictionary from a string.

string = 'w3resource'
my_dict = {}

for l in string:
  my_dict[l] = my_dict.get(l, 0) + 1

print(my_dict)