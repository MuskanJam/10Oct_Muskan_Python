# Write a Python program to find the highest 3 values in a dictionary.

data = {'a':90, 'b':80, 'c':70, 'd':60,'e':50, 'f':40, 'g':30}

largest = sorted(data, key = data.get, reverse=True)

for index in range(3):
  print(largest[index])