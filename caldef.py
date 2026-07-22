def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if op == "+":
    print("Addition =", addition(num1, num2))
elif op == "-":
    print("Subtraction =", subtraction(num1, num2))
elif op == "*":
    print("Multiplication =", multiplication(num1, num2))
elif op == "/":
    print("Division =", division(num1, num2))
else:
    print("Wrong operator")