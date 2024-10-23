from addition import addition
from division import division
from subtraction import subtraction
from multiplication import multiplication
from exponentiation import exponentiation
from sqrt import sqrt

def calculator():
    print("Welcome to the MAD calculator")
    print('''
      _____________________
     |  _________________  |
     | |              0. | |
     | |_________________| |
     |  ___ ___ ___   ___  |
     | | 7 | 8 | 9 | | + | |
     | |___|___|___| |___| |
     | | 4 | 5 | 6 | | - | |
     | |___|___|___| |___| |
     | | 1 | 2 | 3 | | * | |
     | |___|___|___| |___| |
     | | . | 0 | = | | / | |
     | |___|___|___| |___| |
     |_____________________|
    ''')

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    operation = str(input("Enter choice (+, -, *, /, **, ^, sqrt): "))

    if operation == "+":
        return print(f"{n1} + {n2} = {addition(n1,n2)}")
    
    if operation == "-":
        return print(f"{n1} - {n2} = {subtraction(n1,n2)}")

    if operation == "/":
        return print(f"{n1} / {n2} = {division(n1,n2)}")

    if operation == "*":
        return print(f"{n1} * {n2} = {multiplication(n1,n2)}")   
    
    if operation == "**" or  operation == '^':
        return print(f"{n1} * {n2} = {exponentiation(n1,n2)}")  
    
    if operation == "sqrt":
        return print(f"sqrt {n1} = {sqrt(n1)}")  
    


