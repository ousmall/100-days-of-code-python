from calculator_logo import logo
import os

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1 ,n2):
    if n2 != 0:
        return n1 / n2
    else:
        print("Error: Division by zero is not allowed.")
        return None

operations = {
 "+":add,
 "-":subtract,
 "*":multiply,
 "/":divide   
}

def calculator():
    print(logo)
    
    num1 = float(input("Please enter the first number:\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above:\n")
        while not operation_symbol in operations:
            print("You pick an wrong operation, please try again.")
            calculator()
        num2 = float(input("Please enter the next number:\n"))
        calculation_function = operations[operation_symbol]

        result = calculation_function(num1, num2)
        if result is not None:
            print(f"{num1} {operation_symbol} {num2} = {result}")
        else:
            continue
        
        if_continue = input(f"Type 'y' to continue calculating with {result}, or type 'r' to start a new calculation, or type 'n' to exit:\n") 
        if if_continue == "y":
            num1 = result
        elif if_continue == "r":
            os.system("cls" if os.name == "nt" else "clear") # learn from ChatGPT
            calculator() 
        elif if_continue == "n":
            should_continue = False
        else: 
            print("Invalid input. Exiting...")
            should_continue = False
                        
calculator()
