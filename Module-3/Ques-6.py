# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
str = 0
list = ["abc", "abcd", "aa", "abdb", "gssw"]

for x in list:
  if len(x) >=2 and x[0] == x[-1]:
    print(x)
    str = str+1
print("The first and last character are same from a agiven list of strings is:",str)