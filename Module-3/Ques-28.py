#  Write a Python program to remove an empty tuple(s) from a list of tuples. 

list = [("14", "99"),(), ("87", "52"), ("31")]
print(list)
 
for t in list:
  if len(t) == 0:
    list.remove(t)
print(list)