#  Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 

data = {'1':['a', 'b'], '2':['c', 'd']}

l = list(data.values())

for combine in l[1:]:
  for i in l[0]:
    for j in combine:
      print(i+j)