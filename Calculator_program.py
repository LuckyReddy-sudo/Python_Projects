number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation you want(+,-,/,*): ")
total = 0
if operation == '*':
    total = (number1 * number2)
    print(f'Multiplication Total is :{total}')
elif operation == '/':
    total = (number1 / number2)
    print(f'Division Total is :{total}')
elif operation == '+':
    total = (number1 + number2)
    print(f'Addition Total is :{total}')
elif operation == '-':
    total = (number1 - number2)
    print(f'Sub Total is :{total}')
else:
    print("Invalid operator")













