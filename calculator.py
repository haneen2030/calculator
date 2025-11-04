def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
    else:
       result = None

    return result


number1 = float(input('Enter your first number: '))

while True:
    op = input('Welcome, please select your operation (+, -, *, /, **)  ')
    if op in ['+', '-', '*', '/', '**', '^']:
        break
    else:
        print('Invalid choice, please try again.')

number2 = float(input('Enter your second number: '))

print('you entered:', number1,op,number2)
result = calculate(number1 ,number2, op)
print('= ' ,result)
