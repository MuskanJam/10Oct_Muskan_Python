#  Write a Python program to print all unique values in a dictionary. 

dataset=[]

for i in range(3):
  entry=input(f"Enter data for entry {i+1}: ")
  dataset.append(entry)

print("Unique Dataset:", dataset)