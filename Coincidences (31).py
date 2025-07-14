num1 = set(input('Enter st num: '))
num2 = set(input('Enter nd num: '))

num3 = num1 & num2

if len(num3) == 0:
    print('No matches')
else:
    print(num3)