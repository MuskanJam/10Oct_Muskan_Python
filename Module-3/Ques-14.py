#  Write a Python program to find the second smallest number in a list.

list = ['21', '25', '45', '45', '87', '98', '87', '95']

list.remove(min(list))
print(min(list))