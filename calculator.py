def Calculator():

    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operand = input("Enter operator: ")
    
    if operand == '+':
        print(num1 + num2)
    if operand == '-':
        print(num1 - num2)
    if operand == '*':
        print(num1 * num2)
    if operand == '/':
        print(num1 / num2)

Calculator()