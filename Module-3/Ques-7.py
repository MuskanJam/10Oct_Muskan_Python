#  Write a Python program to remove duplicates from a list. 

list = [1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9, 9]
print(list)

for i in range(10):
  res=tuple(set(list))

print("After removing duplicate from a list:", str(res))