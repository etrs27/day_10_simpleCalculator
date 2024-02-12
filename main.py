from art import logo

# Add
def add(num1, num2):
  return num1 + num2

# Subtract
def subtract(num1, num2):
  return num1 - num2

# Multiply
def multiply(num1, num2):
  return num1 * num2

# Divide
def divide(num1, num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

print(logo)
def calculation():
  num1 = float(input("What is the first number?: "))
  for symbol in operations:
    print(symbol)
  continue_op = True
  
  while continue_op:
    chosen_symbol = str(input("Pick an operation symbol from above: "))
    num2 = float(input("What is the second number?: "))
    answer = operations[chosen_symbol](num1, num2)
    print(f"{num1} {chosen_symbol} {num2} = {answer}")
    continued = str(input("Type 'y' to continue the calculation 'y' or type 'n' to start a new calculation: ")).lower()
    
    if continued == "n":
      continue_op = False
      calculation()
    elif continued == "y":
      num1 = answer
    else:
      continue_op = False
      print("Invalid response. Exiting.")

calculation()