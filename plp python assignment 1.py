num_1 = float(input('Enter the first number:'))
num_2 = float(input('Enter the second number:'))
sign = input('Enter operation sign(+, -, *, /):')

if sign == '+':
    print(num_1 + num_2)
elif sign == '-':
    print(num_1 - num_2)
elif sign == '/':
    if num_2 == 0:
        print('The answer is infinity.')
    else:
        print(num_1/num_2)
elif sign == '*':
    print(num_1 * num_2)
else:
    print('System failure')