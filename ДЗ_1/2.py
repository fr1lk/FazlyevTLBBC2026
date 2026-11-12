def multiply(a, b):
    """
    функция умножения
    """
    return a * b
def sum(a, b):
    """
    функция суммы
    """
    return a + b
def subtract(a, b):
    """функция вычитания"""
    return a - b
def div(a, b):
    """функция деления"""
    return a / b
a = int(input())
b = int(input())
c = input()
if c == '+':
    print(sum(a, b))
elif c == '-':
    print(subtract(a, b))
elif c == '*':
    print(multiply(a, b))
elif c == '/':
    print(div(a, b))
else:
    print('ERROR')