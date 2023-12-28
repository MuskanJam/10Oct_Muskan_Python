# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def factorial(num):
  factorial = 1
  if num < 0:
    print("Factorial does not exit for negative number.")
  elif num == 0:
    print("Factorial of 0 is 1.")
  else:
    for i in range(1, num + 1):
      factorial = factorial * i
    print("Factorial of", num, "is", factorial)

n1 = int(input("Enter a number:"))
factorial(n1)