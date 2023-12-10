#  Write a Python program to map two lists into a dictionary.

l1 = ['A', 'B', 'C', 'D']
l2 = [1, 2, 3, 4]

d = {}
for i in range(len(l1)):
  d[l1[i]] = l2[i]
print(d)