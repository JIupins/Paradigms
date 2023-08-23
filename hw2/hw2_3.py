def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Введите число: "))
result = fibonacci(n)
print(f"Число Фибоначчи под номером {n} равно {result}")