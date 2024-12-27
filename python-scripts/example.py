import sys
from datetime import datetime

def greet_user(name):
  print(f"Hello, {name}! Welcome to the Python binary example.")
  print(f"Current date and time: {datetime.now()}")

def calculate_sum(a, b):
  return a + b

def main():
  if len(sys.argv) < 3:
    print("Usage: example.py <name> <num1> <num2>")
    sys.exit(1)

  name = sys.argv[1]
  try:
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
  except ValueError:
    print("Error: num1 and num2 should be numbers.")

  greet_user(name)
  result = calculate_sum(num1, num2)
  print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
  main()
