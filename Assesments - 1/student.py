import student

students = {}

def view_details():
  serial_no = int(input("Enter a Serial Number: "))
  if serial_no in students:
    student = students[serial_no]
    print("Serial Number:", serial_no)
    print("First Name:", student['fname'])
    print("Last Name:", student['lname'])
    print("Contact Number:", student['contact'])
    print("Subjects:")
    for subject, subject in student['subjects'].items():
      print("\tSubject:", subject)
      print("\tMarks:", subject['marks'])
      print("\tFees:", subject['fees'])
  else:
    print("Student with the given Serial Number does not exist.")
    print(students)        