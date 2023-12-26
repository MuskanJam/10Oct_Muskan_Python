import counsellor
students = {}

def add_student():
  serial_no = int(input("Enter a Serial Number: "))
  firstname = str(input("Enter a First Name: "))
  lastname = str(input("Enter a Last Name: "))
  contact_no = input("Enter a Contact Number: ")
  facultyname = input("Enter a faculty name: ")
  while not contact_no.isdigit() or len(contact_no) != 10 or not firstname.isalpha():
    print("Invalid. Please enter valid details.")
    add_student()
    return
      
  subjects = {}
  while True:
    subjectname = str(input("Enter a Subject Name: "))
    if subjectname.lower() == 'done':
      break
    marks = int(input("Enter a Marks: "))
    fees = int(input("Enter a fees: "))
    subjects[subjectname] = {'marks': marks, 'fees': fees}
    students[serial_no] = {
        'fname': firstname,
        'lname': lastname,
        'contact': contact_no,
        'subject': subjects,
        'faculty': facultyname
      }
  print("Student has been added successfully.")
  print(students)
    
def remove_student():
  serial_no = int(input("Enter a Serial Number to remove: "))
  if serial_no in students:
    del students[serial_no]
    print("Student is removed successfully.")
  else:
    print("Student not found.")
    print(students)

def view_all():
  for serial_no, student in students.items():
    print("Serial Number:", serial_no)
    print("First Name:", student['fname'])
    print("Last Name:", student['lname'])
    print("Contact Number:", student['contact'])
    print("Subjects:")
    for subject, subject in student['subjects'].items():
      print("\tSubject:", subject)
      print("\tMarks:", subject['marks'])
      print("\tFees:", subject['fees'])
    print()
    print(students)

def view_specific():
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