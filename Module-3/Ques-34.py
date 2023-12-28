#  Write a Python script to check if a given key already exists in a dictionary. 

a = {'a':90, 'b':80, 'c':70, 'd':60,'e':50, 'f':40, 'g':30}

x = input("Enter key:")
if x in a:
  print("Yes, it exists.")
else:
  print("Not exists.")