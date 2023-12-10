#  Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.
def swap(str1, str2):
  print(f"{str1 + str2}")
  print(f"{str1[2:] + str2[:2]}")

str1 = input("Enter the first string:")
str2 = input("Enter the second string:")

result = swap(str1, str2)