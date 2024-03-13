# Write a Python program to write a list to a file. 
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

with open('fruits.txt', 'w') as file:
  for item in my_list:
    file.write(item + '\n')

print("List written to the file successfully.")