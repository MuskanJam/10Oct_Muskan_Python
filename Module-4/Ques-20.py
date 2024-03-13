# Write python program that user to enter only odd numbers, else will raise an exception. 

class EvenNumberError(Exception):
  def __init__(self, value):
    self.value = value

try:
  while True:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
      raise EvenNumberError(num)
    else:
      print("You entered an odd number. Well done!")
      break
except EvenNumberError as e:
  print(f"Error: {e.value} is not an odd number. Please enter an odd number.")
except ValueError:
  print("Error: Please enter a valid integer.")
