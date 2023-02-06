import random

def zadacha1():
    # Задача 1. В каждой группе учится от 20 до 30 студентов. 
    # По итогам экзамена все оценки заносятся в таблицу. 
    # Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
    group_count=4
    marks = [0] * group_count

    for i in range(group_count):
        marks[i]= [random.randint(2,5) for _ in range(random.randint(20, 30))]

    for row in marks:
        print(row)

    mark_max = 0
    group_max = 0

    for i in range(group_count):
        average_mark = 0
        students_count= len(marks[i])
        for j in range(students_count):
            average_mark += marks[i][j]
        average_mark /= students_count
        if average_mark > mark_max:
            mark_max = average_mark
            group_max = i+1

    print(f"Максимальный средний бал у группы {group_max}")

def zadacha2():
    # Задача 2. Дана квадратная матрица, заполненная случайными числами. 
    # Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
    rows = 4
    numbers = [0]*rows

    for i in range(rows):
        numbers[i] = [random.randint(1, 100) for _ in range(rows)]

    for row in numbers:
        print(row)

    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += numbers[i][i]
    print(f"Сумма элементов главной диагонали равна {diagonal_sum}")

    for index in range(len(numbers)):
        sum_in_row = sum(numbers[index])
        if sum_in_row > diagonal_sum:
            print(f"{index+1}, {numbers[index]} = {sum_in_row}")

#Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.

def periods_for_month(temp_in_month, period, month):
    max_temp = 0
    day_max_temp = 1
    min_temp = 100
    day_min_temp = 1
    

    for day in range(len(temp_in_month) - period +1):
        temp_in_period = temp_in_month[day: day + period]
        sum_temp_in_period = sum(temp_in_period)
        print(f"{day+1} - {day+period}. {temp_in_period} {sum_temp_in_period}")
        if sum_temp_in_period > max_temp:
            max_temp = sum_temp_in_period
            day_max_temp = day
        elif sum_temp_in_period < min_temp:
            min_temp = sum_temp_in_period
            day_min_temp = day

    print(f"Максимальная температура {round(max_temp/period, 1)} была с {day_max_temp + 1} по {day_max_temp + period} {month}")
    print(f"Минимальная температура {round(min_temp/period, 1)} была с {day_min_temp + 1} по {day_min_temp + period} {month}")

def zadacha3():
#для одного месяца
    temp_in_month = [random.randint(18,32) for _ in range(31)]
    print(f"Все температуры {temp_in_month}")
    period = 7
    periods_for_month(temp_in_month, period, "мая")