# Write a Python program to count the frequency of words in a file. 
with open("example.txt", "r") as file:
  text = file.read()
words = text.split()

word_freq = {}

for word in words:
  if word in word_freq:
    word_freq[word] += 1
  else:
    word_freq[word] = 1


print("Word frequencies in the file:")
for word, freq in word_freq.items():
  print(f"{word}: {freq}")