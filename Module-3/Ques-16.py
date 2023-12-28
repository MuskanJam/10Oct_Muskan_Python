#  Write a Python program to check whether a list contains a sub list.

list = [[1, 2, 4], [7, 8, 9, 3], ['m', 5, 6, 4, 2]]

count = 0

for i in list:
  if len(i) > 1:
    count += 1
    print(f"{count} sublist of list:", i)
    print()
  else:
    continue