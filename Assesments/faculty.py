import logging

students = {}
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_transaction(message):
  logging.info(message)

def add_marks():
    facultyname = input("Enter a faculty name: ")
    serial_no = int(input("Enter Serial number: "))

    if serial_no in students and students[serial_no]['faculty'] == facultyname:
      subjectname = input("Enter a Subject Name: ")
      marks = int(input("Enter a Marks: "))

      if subjectname in students[serial_no]['subject']:
        students[serial_no]['subject': subjectname]['marks'] =  marks
        print("Marks added successfully.")
        log_transaction(f"Faculty {facultyname} added marks for Student: {serial_no} in {subjectname}.")
      else:
        print("Marks already exists.")
    else:
      print("Student not found.")
      print(students)
        
def view_all():
  faculty_name = input("Enter your Faculty Name: ")
  print(f"All Students in {faculty_name}'s faculty:{students}")
    
  for serial, student in students.items():
    if student['faculty'] == faculty_name:
      print(f"{serial}: {student}")
      print(students)