# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2 
# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0

import random

def CreateArray(length):
    array = []
    for i in range(length + 1):
        array.append(random.randint(0, 100))
    return array

def Polynomial(array):
    length = len(array)
    polynom = []
    for i in range(len(array)):
        length -= 1
        if array[i] == 1:
            polynom.append('x' + ' * x' * (length - 1) + ' + ')
        elif array[i] > 1:
            polynom.append(str(array[i]))
            polynom.append(' * x' * length + ' + ')
    polynom.pop(-1)
    return polynom
        
degree = int(input('Введите натуральную степень многочлена > '))
coefficient = CreateArray(degree)
print(coefficient)
result = ''.join(Polynomial(coefficient))

with open('file1.txt', 'w') as data:
    data.write(result)
