# Write a Python program to replace last value of tuples in a list. 

x = [("1", "2", "4", "8")]
print(x)
for t in x:
  print([t[:3] + ("10",)] )