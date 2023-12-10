# Write a Python script to concatenate following dictionaries to create a new one.

a = {1:90, 2:80}
b = {3:70, 4:60}
c = {5:50, 6:40, 7:30}

e = {}

print("a=", a)
print("b=", b)
print("c=", c)

for i in (a, b, c):
  e.update(i)

print(e)