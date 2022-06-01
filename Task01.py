def CalculatePi(accuracy):
    myPi = 3
    temp = 0
    myAccuracy = 10**(-accuracy)
    i = 2
    sign = 1
    while abs(myPi - temp) > myAccuracy:
        temp = myPi
        myPi = myPi + sign * 4 / (i * (i+1) * (i+2))
        sign = -sign
        i += 2
    return round(myPi, accuracy)
try:
    print('==========Задача № 1==========')
    print('Ввычислить число pi, c заданной точностью d')
    accuracy = int(input('Введите точность вычисления числа pi (1 - 10): '))
    if  0 < accuracy <= 10:
        print(f'Число pi = {CalculatePi(accuracy)}')
    else:
        print('Значение точности должно быть от 1 до 10')
except ValueError:
    print('Введено не число')