def zadacha1():
    N= int(input("Введите число: "))
    count = N
    num_first = 0
    num_second = 1
    data = open("fibonacci.txt", mode= "w", encoding = "utf-8")
    for _ in range(count):
        data.write(str(num_first) + "\n")
        num_first, num_second = num_second, num_first + num_second
    data.close()

def zadacha2():
    data= open("fruits.txt", encoding= "utf-8")
    fruits_list= data.readlines()[0].split(" ")
    data.close()
    print(fruits_list)
    letter = str(input("Введите букву: "))
    for fruit in fruits_list:
        if fruit[0] == letter:
            print(fruit)

def zadacha3():
    phrase_dictionary = \
        {
            "привет" : "добрый день",
            "как тебя зовут?" : "меня зовут Мини-Бот",
            "как дела?" : "спасибо, все отлично"
        }
    start_dialogue = True
    while start_dialogue:
        phrase = input("Я: ")
        phrase = phrase.lower()
        if phrase in phrase_dictionary.keys():
            print(f"Бот: {phrase_dictionary[phrase]}")
        else:
            print("Бот: Я тебя не понимаю, скажи что-то другое")
        if phrase == "пока":
            start_dialogue = False