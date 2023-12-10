# Write a python program to count the number of character(character frequency)in a string.
str=input("Enter any string:")

char_frequency = {char: str.count(char) for char in set(str)}
print("Character frequency in the string:")

for char, frequency in char_frequency.items():
  print(f"{char}: {frequency}")