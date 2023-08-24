def find_max_imp(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def find_max_dec(numbers):
    return max(numbers)


num1 = (1, 2, 3, 4, 53, 6, 7, 8)
num2 = (2, 2, 3, 4, 22, 6, 7, 8, 9)

max_imp = find_max_imp(num1)
max_dec = find_max_dec(num2)

print(f"Императивное решение (нахождение максимального числа): {max_imp}")
print(f"Декларативное решение (нахождение максимального числа): {max_dec}")