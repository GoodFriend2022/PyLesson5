# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def Exponentiation(number, degree):
    if degree < 0:
        exp = Exponentiation(number, degree + 1) / number
    elif degree == 0:
        return 1
    elif degree == 1:
        return number
    else:
        exp = Exponentiation(number, degree - 1) * number
    return exp
    
def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

firstNumber = input('Введите первое целое число > ')
secondNumber = input('Введите второе целое число > ')
if isInt(firstNumber) and isInt(secondNumber):
    print(Exponentiation(int(firstNumber), int(secondNumber)))
else:
    print('Необходимо ввести ЦЕЛЫЕ ЧИСЛА! Перезапустите программу и попробуйте ещё раз')


