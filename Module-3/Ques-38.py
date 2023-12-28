# Write a Python program to check multiple keys exists in a dictionary.

x = {
  'class': 'A', 'id': '5'
}

print(x.keys() >= {'class', 'name'})
print(x.keys() >= {'id', 'name'})