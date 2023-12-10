#  Write a Python script to sort (ascending and descending) a dictionary by value. 

marks = {"Muskan":90, "Suzan":80, "Hasti":85}
print(marks)

result = sorted(marks.items(), key = lambda x: x[1])
print(result)