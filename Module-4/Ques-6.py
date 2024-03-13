# Write a Python program to read a file line by line and store it into a list.
with open("example.txt", "r") as file:
    lines = []
    for line in file:
        line = line.strip("\n")
        lines.append(line)

print("Lines in the file:")
for line in lines:
    print(line)