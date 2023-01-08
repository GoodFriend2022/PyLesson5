# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится 
# запись многочлена (полученные в результате работы программы из задачи 103). 
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

x = int(input('Чему равен х = '))

data = open('file1.txt', 'r')
for i in data:
    poly = i
poly = poly.replace('x', f'{x}')

poly = poly.split(' ')

print(poly)
