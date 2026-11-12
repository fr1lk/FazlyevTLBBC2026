a = int(input())
b = int(input())
c = input()
#enter the numbers and the sign
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif (c == '/') and (b != 0):
    print(a / b)
else:
    print('ERROR')
#we receive a response