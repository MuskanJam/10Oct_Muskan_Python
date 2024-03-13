# Write a Python program to count the number of lines in a text file.

with open("example.txt", "r") as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f"The file contains {line_count} lines.")