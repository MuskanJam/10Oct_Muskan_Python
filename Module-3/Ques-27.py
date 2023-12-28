#  Write a Python program to find the repeated items of a tuple.

tuple = ("Strawberry", "21", "48", "Muskan", "Litchi", "48")
# l = []

# for i in tuple:
#   if tuple.count(i) > 1:
#     if i not in l:
#       l.append(i)

# print("Repeated items:", l)


count = tuple.count("48")
print(count)