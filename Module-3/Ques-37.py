# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 

d = {}

n = int(input("Enter a number:"))

for x in range(1, 15):
  d[x] = x*x

print(d)