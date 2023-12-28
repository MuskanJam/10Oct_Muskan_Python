# Write a Python program to convert a list of tuples into a dictionary. 

l = [("a", 1), ("b", 2), ("c", 3), ("d", 5)]
d = {}

for x, y in l:
  d.setdefault(x, []).append(y)
print(d)