# Write a Python program to read last n lines of a file. 
with open("example.txt", "r") as file:
    n = int(input("Enter the number of lines to read from the end: "))
    lines = file.readlines()
    last_n_lines = lines[-n:]

    print("The last", n, "lines of the file are:")
    for line in last_n_lines:
        print(line, end="")