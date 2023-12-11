#  Write a Python program to combine values in python list of dictionaries.

from collections import defaultdict
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] 

new_data = defaultdict(int)
for a in data:
  new_data[a['item']] += a['amount']
print("Counter", dict(new_data))