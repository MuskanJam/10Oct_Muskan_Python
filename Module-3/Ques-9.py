#  Write a Python function that takes two lists and returns true if they have at least one common member.

list1 = [10, 28, 4, 50]
list2 = [1, 2, 3, 4, 5]

for x in list1:
  for y in list2:
    if x == y :
      print("True")