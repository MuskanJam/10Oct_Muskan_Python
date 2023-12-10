# Write a Python program to get unique values from a list.

list = [1, 4, 8, 7, 9, 2, 6, 3, 4, 5, 8]
print(list)

unique = []
for i in list:
  if i not in unique:
     unique.append(i)
print(unique)