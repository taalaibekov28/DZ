class MyCount:
    def init(self, x):
        self.x = x

    # Сложение
    def add(self, other):
        return self.x + other.x

    # Вычитание
    def sub(self, other):
        return self.x - other.x

    # Умножение
    def mul(self, other):
        return self.x * other.x

    # Деление
    def truediv(self, other):
        return self.x / other.x

    # Целочисленное деление
    def floordiv(self, other):
        return self.x // other.x

    # Остаток
    def mod(self, other):
        return self.x % other.x

    # Возведение в степень
    def pow(self, power, modulo=None):
        return self.x,  power.x


a = MyCount(3)
b = MyCount(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a,  b)