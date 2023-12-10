#  Write a Python function to insert a string in the middle of a string.
str = "Hello My name is Muskan"
insert = "\tWorld!"

result = str[:5] + insert + str[5:]
print(result)