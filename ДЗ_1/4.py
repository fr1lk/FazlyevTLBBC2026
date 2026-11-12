class Calculador:
    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

calc = Calculador()
print(calc.sum(10, 20))
print(calc.sub(10, 20))
print(calc.mul(10, 20))
print(calc.div(10, 20))