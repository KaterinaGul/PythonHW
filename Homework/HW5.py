import random
def zadacha1():
    # Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
    # 2, 3, 4, 6, 7, 8 -> 6, 7, 8
    numbers = list(random.randint(1,100) for _ in range (random.randint(3,21)))
    print(f"Список случайных чисел: {numbers}")
    result = list(filter(lambda x:x >5, numbers))
    print(f"Элементы больше пяти: {result}")

def zadacha2():
    # Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
    # [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
    numbers = list(random.randint(1,100) for _ in range (random.randint(1,21)))
    print(f"Список случайных чисел: {numbers}")
    index = random.randint (0, len(numbers) -1)
    result = [numbers[index]]
    while index < len(numbers):
        index = random.randint(index, len(numbers))
        if index!= len(numbers) and numbers[index] > result[-1]:
            result.append(numbers[index])
    print(result)

def zadacha3():
    # Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
    # [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
    # [1, 4, 2, 3, 6, 7]
    numbers = list(random.randint(1,10) for _ in range (random.randint(1,21)))
    print(f"Список случайных чисел: {numbers}")
    print(f"Список уникальных элементов: {set(numbers)}")

    result = list(filter(lambda x:numbers.count(x) > 1, numbers))
    result = list(map(lambda x:numbers.count(x) > 1, numbers))
    print(f"Количество повторений в списке: {result.count(True)}")