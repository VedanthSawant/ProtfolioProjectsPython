import MyModule
print(MyModule.calculator_logo)
continue_YN = 'y'

def addition(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

num1 = float(input("What's the first number?: "))
while continue_YN == 'y':
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = float(input("What's the next number?: "))
    if operation == "+":
        result = addition(num1, num2)
    elif operation == "-":
        result = substraction(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    continue_YN = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation. ")
    if continue_YN == 'y':
        num1 = result
