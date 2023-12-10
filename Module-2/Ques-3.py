# Write a python program to get Fibonacci series of given range.
def fibo(n):
  series = [0,1]

  for i in range(2, n):
    series.append(series[-1] + series[-2])
  print(series)
  
num=int(input("Enter a number:"))

result= fibo(num)