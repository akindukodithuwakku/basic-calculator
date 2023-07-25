import os

from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def devide(n1 , n2):
  return n1 / n2

def multiply(n1 , n2):
  return n1 * n2

def subtraction(n1,n2):
  return n1 - n2

operations = {
  "+" : add,
  "-" : subtraction,
  "/": devide,
  "*": multiply
  
}

user_continue = True

while user_continue == True:
  

  number1 = int(input("enter the first number:  "))
  number2 = int(input("enter the second number: "))
  for symbol in operations:
    print(symbol)
  calculation_symbol = input("select one symbol from the above list: ")
  if calculation_symbol not in operations:
    print("you entered an invalid operator")
  
  
  calculation = operations[calculation_symbol]
  
  answer = calculation(number1,number2)
  
  print(f"{number1} {calculation_symbol} {number2} = {answer}")
  continue_calculation = input("Do you want to perform another calculation: Type 'y' to continue, 'n' to terminate the operation: ").lower()
  os.system('clear')
  from art import logo
  
  if continue_calculation == "n":
    user_continue = False
    print("Good Bye! ")
