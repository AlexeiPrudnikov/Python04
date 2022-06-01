def Divisors(n):
    divisors = []
    divisors.append(1)
    if n > 1:
        i = 2
        while i <= (n ** 0.5):
            if (n % i) == 0:
                divisors.append(i)
                if i != (n // i):
                    divisors.append(n // i)
            i += 1
        divisors.append(n)
        divisors.sort()
    return divisors
try:
    print('==========Задача № 2==========')
    print('Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.')
    n = int(input('Введите число N: '))
    if  0 < n:
        print(f'Простые множители числа {n} -> {Divisors(n)}')
    else:
        print('Значение должно быть натуральным.')
except ValueError:
    print('Введено не число')