import random
minValue = -10
maxValue = 10
def UniqueElements(intList):
    return [i for i in intList if intList.count(i) == 1]
try:
    print('==========Задача № 3==========')
    print('Вывод неповторяющихся элементов исходной последовательности')
    countElements = int(input('Введите длину последовательности: '))
    if countElements > 0:
        print(f'Производится генерация последовательности длины {countElements}...')
        intList = []
        for i in range(countElements):
            intList.append(random.randint(minValue, maxValue))
        print(intList)
        print('Уникальные элементы последовательности...')
        print(UniqueElements(intList))
    else:
        print('Число элементов должно быть больше 0')
except ValueError:
    print('Введено не число')