# Write a python program to find the longest words. 
with open("example.txt", "r") as file:
  text = file.read()

words = text.split()
max_length = max(len(word) for word in words)
longest_words = []

for word in words:
  if len(word) == max_length:
    longest_words.append(word)
print("The longest word(s) in the file are:")
for word in longest_words:
  print(word)