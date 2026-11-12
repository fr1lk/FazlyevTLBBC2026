def calc(a, c, b):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        return  'ERROR'

while True:
    a, c, b = input().split()
    print(calc(int(a), str(c), int(b)))