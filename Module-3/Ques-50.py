#  Write a Python function to check whether a number is perfect or not. 

n = int(input("Enter a number:"))
result = 0
for i in range(1, n):
  if (n % i) == 0:
    result = result + i
if result == n:
  print(n, "is perfect number.")
else:
  print(n, "is not perfect number.")