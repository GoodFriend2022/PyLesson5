# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def Sum(a, b):
    if b == 0:
        return a
    else:
        sum = Sum(a, b - 1) + 1
    return sum

def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

firstNumber = input('Введите первое целое неотрицательное число > ')
secondNumber = input('Введите второе целое неотрицательное число > ')
if isInt(firstNumber) and isInt(secondNumber) and int(firstNumber) >= 0 and int(secondNumber) >= 0:
    print(Sum(int(firstNumber), int(secondNumber)))
else:
    print('Необходимо ввести ЦЕЛЫЕ НЕОТРИЦАТЕЛЬНЫЕ ЧИСЛА!' +
    'Перезапустите программу и попробуйте ещё раз')