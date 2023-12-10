# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def replace(str):
  str_not = str.find('not')
  str_poor = str.find('poor')

  if str_not < str_poor:
    print(str[:str_not] + 'good' + str[str_poor + 4:])
  else:
    print(str)

a=input("Enter a string:")

result = replace(a)