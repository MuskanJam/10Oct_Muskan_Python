# Write a Python program to copy the contents of a file to another file. 
with open('source.txt', 'r') as source_file:
  with open('destination.txt', 'w') as dest_file:
    contents = source_file.read()
    dest_file.write(contents)

print("File contents copied successfully.")