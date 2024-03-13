# Write a Python program to append text to a file and display the text. 
with open("example.txt", "a") as file:
    file.write("This is a new Python module number 4.\n")
    file.write("And learn about advanced python programming.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)