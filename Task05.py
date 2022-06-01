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
def ReadPolynomial (path):
    file = open(path, 'r')
    polynomial = file.read();
    file.close()
    temp = polynomial.split(' + ')
    cfList = []
    for i in temp:
        cfList.append(i.split('x')[0])
    cfList.reverse()
    cfList[0] = cfList[0].split(' = ')[0]
    return list(map(int, cfList))
def SummPolynomial (poly1, poly2):
    result = []
    length = min(len(poly1), len(poly2))
    for i in range(length):
        result.append(poly1[i] + poly2[i])
    temp = []
    if len(poly1) < len(poly2):
        temp = poly2
    elif len(poly1) > len(poly2):
        temp = poly1
    for i in range(length, len(temp)):
        result.append(temp[i])
    return result
try:
    print('==========Задача № 5==========')
    print('Генерация многосчена степени N')
    n = int(input('Введите степень 1 многочлена: '))
    m = int(input('Введите степень 2 многочлена: '))
    if m > 0 and n > 0:
        print(f'Производится генерация многослена степени {n}...')
        coeffList = [random.randint(minValue, maxValue) for i in range(n + 1)]
        path = 'Polynomial_1.txt'
        file = open(path, 'w')
        file.write(GetPolynomial(coeffList))
        file.close()
        print(f'Многочлен {GetPolynomial(coeffList)} записан в файл {path}')
        print(f'Производится генерация многослена степени {m}...')
        coeffList = [random.randint(minValue, maxValue) for i in range(m + 1)]
        path = 'Polynomial_2.txt'
        file = open (path, 'w')
        file.write(GetPolynomial(coeffList))
        file.close()
        print(f'Многочлен {GetPolynomial(coeffList)} записан в файл {path}')
        print('Производится считывание многочленов из файлов и их суммирование...')
        summPoly = SummPolynomial(ReadPolynomial('Polynomial_1.txt'), ReadPolynomial('Polynomial_2.txt'))
        print(f'Сумма многочленов равна {GetPolynomial(summPoly)} ')
    elif n <= 0 and m > 0:
        print('Степень 1 многочлена должна быть больше 0')
    elif m <= 0 and n > 0:
        print('Степень 2 многочлена должна быть больше 0')
    else:
        print('Степени многочленов должны быть больше 0')
except ValueError:
    print('Введено не число')