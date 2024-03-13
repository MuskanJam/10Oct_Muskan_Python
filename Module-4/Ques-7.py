# Write a Python program to read a file line by line store it into a variable. 

with open("example.txt", "r") as file:

    line1 = "Hello!This is Python course."
    line2 = "My name is Muskan."
    line3 = "This is a new Python module number 4."
    line4 = "And learn about advanced python programming."

    line_number = 1
    for line in file:
        line = line.strip("\n")
        if line_number == 1:
            line1 = line
        elif line_number == 2:
            line2 = line
        elif line_number == 3:
            line3 = line
        elif line_number == 4:
            line4 = line
        else:
            break  
        line_number += 1

print("Line 1:", line1)
print("Line 2:", line2)
print("Line 3:", line3)
print("Line 4:", line4)