# Задача 102 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def Multipliers(number):
    multipliers = []
    mult = 2
    while mult <= number:
        while number % mult == 0:
            multipliers.append(mult)
            number /= mult
        mult += 1
    return multipliers

n = int(input('Введите число которое хотите разложить на простые множители > '))
print(Multipliers(n))
