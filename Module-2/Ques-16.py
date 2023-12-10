# Write a Python program to count the occurrences of each word in a given sentence.
str=input("Enter any string:")
word = {word: str.count(word) for word in set(str)}

for word, frequency in word.items():
  print(f"{word}: {frequency}")