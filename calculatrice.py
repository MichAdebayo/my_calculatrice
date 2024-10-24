from addition import addition
from division import division
from subtraction import subtraction
from multiplication import multiplication
from exponentiation import exponentiation
from sqrt import sqrt
from history import history

def calculator():

    l = []
    operations = ["+", "-" , "*" , "/" , "**" , "^" , "sqrt"]

    while True:
        
        try:            
            
            operation = str(input("Enter choice (+, -, *, /, **, ^, sqrt): "))

            if operation in operations:
                break
            else:
                raise ValueError
        
        except ValueError:
                print("Enter a valid operation")
    
    while True:

        if operation == 'sqrt':
            n1 = float(input("Enter a number: "))
            result = {sqrt(n1)} 
            print(f'''
            _____________________
            |  _________________  |
            | |{result}         | |
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
        
            l.append(history("sqrt", n1, result=result))
        else:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            result = None
        
            if operation == "+":
                result = addition(n1,n2)

            elif operation == "-":
                result = subtraction(n1,n2)


            elif operation == "/":
                result = division(n1,n2)

            elif operation == "*":
                result = multiplication(n1,n2)
            
            elif operation == "**" or  operation == '^':
                result = exponentiation(n1,n2)
            
            else:
                print("Error: enter correct operation")

            if result is not None:
                print(f'''
                _____________________
                |  _________________  |
                | |{result}         | |
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

                l.append(history(operation, n1, n2, result))


        next_calculation = str(input("Do you want to perform another calculation? (yes/no): "))

        if next_calculation.lower() != 'yes':
            print("Fermeture du supercalculateur MAD")
            
            # Write to log file
            with open("log_calculations.txt", "w") as f:
                for entry in l:
                    f.write(entry + "\n")  # Ensure each entry is a string
            break
        



        
        

    