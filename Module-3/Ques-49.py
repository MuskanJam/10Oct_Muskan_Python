#  Write a Python function to check whether a number is in a given range.

def range(num, start, end):
  if start <= num <= end:
    print(True)
  print(False)

n = int(input("Enter a number:"))
starting_range = int(input("Enter a starting range:"))
ending_range = int(input("Enter a ending range:"))

x = range(n, starting_range, ending_range)
if x:
  print("In a given range.")
else:
  print("Not a given range.")
