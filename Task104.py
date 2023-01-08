# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится 
# запись многочлена (полученные в результате работы программы из задачи 103). 
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

def ResultPoly(polinomial):
    multiplication = int(polinomial[0])
    sum = 0
    for i in range(len(polinomial)):
        if polinomial[i] == '*':
            multiplication *= int(polinomial[i + 1])
        elif polinomial[i] == '+':
            sum += multiplication
            multiplication = int(polinomial[i + 1])
    sum += multiplication
    return sum

x = int(input('Чему равен х = '))

data = open('file1.txt', 'r')
for i in data:
    poly = i
poly = poly.replace('x', f'{x}')
poly = poly.split(' ')

print(poly)
result = f'Sum = {ResultPoly(poly)}'

with open('file_sum.txt', 'w') as data:
    data.write(result)