# Задача 101 Вычислить число π c заданной точностью d

# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

import math

def Rounding(number, precision):
    count = 0
    while precision < 1:
        count += 1
        precision *= 10
    return round(number, count)

d = float(input('Введите желаемую точность вывода числа ПИ > '))

print(Rounding(math.pi, d))