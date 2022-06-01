import random
minValue = 0
maxValue = 100
def GetPolynomial(coeffList):
    n = len(coeffList) - 1
    polynomial = ''
    while n >= 2:
        polynomial = polynomial + f'{coeffList[n]}x^{n} + '
        n -=1
    polynomial += f'{coeffList[1]}x + {coeffList[0]} = 0'
    return polynomial
try:
    print('==========Задача № 4==========')
    print('Генерация многосчена степени N')
    n = int(input('Введите степень многочлена: '))
    if n > 0:
        print(f'Производится генерация многослена степени {n}...')
        coeffList = [random.randint(minValue, maxValue) for i in range(n + 1)]
        path = 'Polynomial.txt'
        file = open (path, 'w')
        file.write(GetPolynomial(coeffList))
        file.close()
        print(f'Многочлен {GetPolynomial(coeffList)} записан в файл {path}')
    else:
        print('Степень многочлена должна быть больше 0')
except ValueError:
    print('Введено не число')