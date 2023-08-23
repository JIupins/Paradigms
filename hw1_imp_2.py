# -*- coding: windows-1251 -*-

def find_minimum_number(numbers1):
    min_number = numbers1[0]
    for number1 in numbers:
        if number1 < min_number:
            min_number = number1
    return min_number


numbers = [5, 2, 8, 3, 9, 4]
result = find_minimum_number(numbers)
print("Наименьшее число в списке:", result)