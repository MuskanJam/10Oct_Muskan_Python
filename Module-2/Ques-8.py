#Write a python program to test whether a passed letter is a vowel or not.

char=input("Enter any character:")

vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if char in vowels:
  print("The character is a vowel!") 
else:
  print("The character is not a vowel!") 