# -*- coding: windows-1251 -*-

def sum_of_even_numbers(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum


n = int(input("������� ����� N: "))
result = sum_of_even_numbers(n)
print("����� ������ ����� �� 1 ��", n, ":", result)