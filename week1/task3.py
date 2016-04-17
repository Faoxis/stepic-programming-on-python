x = float(input())
y = float(input())
action = str(input())

if action == '+':
    print(x+y)
elif action == '-':
        print(x - y)
elif action == '/':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x / y)
elif action == '*':
    print(x * y)
elif action == 'mod':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x % y)
elif action == 'pow':
    print(x ** y)
elif action == 'div':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x // y)

