from counsellor import *
from faculty import *
from student import *

print("\t\tpress 1 for Counsellor\n\t\tpress 2 for Faculty\n\t\tpress 3 for Student")
role = int(input("Enter a role id: "))
if role == 1:
  while True:
    print("\t\t1. Add student\n\t\t2. Remove student\n\t\t3. View all students\n\t\t4. View specific student")
    choice = int(input("Enter a choice by counsellor: "))
    if choice == 1:
      add_student()
    elif choice == 2:
      remove_student()
    elif choice == 3:
      view_all()
    elif choice == 4:
      view_specific()
    else:
      print("Invalid choice.")
    more_operation = input("Do you want to perform any more operations? (y/n): ")
    if more_operation != 'y':
      break

elif role == 2:
  while True:
    print("\t\t1. Add marks to student\n\t\t2. View all students")
    choice = int(input("Enter a choice by Faculty: "))
    if choice == 1:
      add_marks()        
    elif choice == 2:
      view_all()
    else:
      print("Invalid choice.")
      more_operation = input("Do you want to perform any more operations? (y/n): ")
      if more_operation != 'y':
        break

elif role == 3:
  while True:
    print("Get details.")
    choice = input("Enter your serial number to get your details: ")
    if choice in students:
      view_details()
    else:
      print("Invalid serial number.")
      break
