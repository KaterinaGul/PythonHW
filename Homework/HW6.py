import random
def zadacha1():
    # Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
    # N может быть любой длины.
    # N = 132: 132 + 132132 + 132132132 = 132264396
    number = input("Введите число: ")
    print(int(number*3) + int(number*2) + int(number))

def zadacha2():
    # Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное 
    # #натуральное число. Напишите программу, которая определяет, есть в массиве 
    # #последовательность из трёх элементов, совпадающая с введённым числом.
    # [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
    # [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
    numbers_list = [random.randint(0,9) for _ in range(15)]
    print(numbers_list)
    number = int(input("Ведите число:"))
    result = ""
    for el in numbers_list:
        result += str(el)
    print(result)

    if str(number) in result:
        print("Такая последовательность есть")
    else:
        print("Совпадений в массиве нет")

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель 
# которых не превышает 11.
def check_numbers(x, y):
    min_number = min(x, y)
    divider = 1
    for el in range(2, min_number+1):
        if x % el == 0 and y % el == 0:
            divider = el
            break
    return divider == 1

def zadacha3():
    for y in range(1, 12):
        for x in range(1, y):
            if check_numbers(x, y):
                print(f"{x}/{y}" , end= " ")
        print()
zadacha3()