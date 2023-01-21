def zadacha1():
#Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#60 -> 2, 2, 3, 5
    number = 60
    multipliers_list = []
    for i in range(2, number):
        while number % i == 0:
            multipliers_list.append(i)
            number//= i
    print(multipliers_list)
    
def zadacha2():
# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»
    data = open('ice_cream.txt', mode='r', encoding='utf-8')
    list = data.readlines()
    data.close()

    ice_cream_range = set(list[0].split(', '))
    ice_cream_available = set(list[1].split(', '))

    print(ice_cream_range.difference(ice_cream_available))

def zadacha3():
#Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
#3 -> 3.142
    import math
    number_of_symbols = int(input("Введите количество символов после запятой в числе пи: "))
    print(round(math.pi, number_of_symbols))
