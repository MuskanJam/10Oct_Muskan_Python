# Write a Python program to read first n lines of a file
with open("example.txt", "r") as file:
    n = int(input("Enter the number of lines to read: "))
    lines = [next(file) for _ in range(n)]

    for line in lines:
        print(line, end="")