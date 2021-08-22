def add(a,b):
    addition = a + b
    print(f"The sum of {a} and {b} is {addition}")
def subtract(a,b):
    subtraction = a - b
    print(f"The result after subtracting {b} from {a} is {subtraction}")
def multiply(a,b):
    multiplication = a * b
    print(f"The multiplication of {a} and {b} is {multiplication}")
def division(a,b):
    division = a / b
    print(f"The result after dividing  {a} with {b} is {division}")

number1,operator,number2 = map(str, input("Enter your equation: ").split()) # 8 / 9
number1 = int(number1)
number2 = int(number2)

if operator == '+':
    add(number1,number2)
elif operator == '-':
    subtract(number1,number2)
elif operator == '*':
    multiply(number1,number2)
elif operator == '/':
    division(number1,number2)
else:
    print("It is invalid, please try again")