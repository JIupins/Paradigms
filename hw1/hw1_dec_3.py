# -*- coding: windows-1251 -*-

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Введите число N: "))
result = factorial(n)
print("Факториал числа", n, ":", result)