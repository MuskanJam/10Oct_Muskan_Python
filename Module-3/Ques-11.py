#  Write a Python function that takes a list and returns a new list with unique elements of the first list.

list = [1, 2 ,4, 2, 6, 5, 7, 6]
print(list)

unique_list=[]

for a in list:
  if a not in unique_list:
    unique_list.append(a)
print("The unique list is:", unique_list)