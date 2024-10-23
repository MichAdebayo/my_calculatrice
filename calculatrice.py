from addition import addition
from division import division
from subtraction import subtraction
from multiplication import multiplication

def calculator():
    print("Welcome to the MAD calculator")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    operation = str(input("Enter choice (+, -, *, /): "))

    if operation == "+":
        return print(f"{n1} + {n2} = {addition(n1,n2)}")
    
    if operation == "-":
        return print(f"{n1} - {n2} = {substraction(n1,n2)}")

    if operation == "/":
        return print(f"{n1} / {n2} = {division(n1,n2)}")

    if operation == "*":
        return print(f"{n1} * {n2} = {multiplication(n1,n2)}")   
    


