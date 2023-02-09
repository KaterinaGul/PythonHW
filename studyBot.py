import telebot
import requests
import random
from telebot import types

game_started = False
r_number = None

bot = telebot.TeleBot("", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Напиши мне: ~погода~ или ~играть~ или ~вычислить математическое выражение~")




@bot.message_handler(content_types=["text"])
def text_commands_from_user(message):
    global game_started
    global r_number

    if message.text == "погода":
        data = requests.get("https://wttr.in/?format=3")
        bot.reply_to(message, data.text)

    elif message.text == "играть":
        if not game_started:
            game_started = True
            r_number = random.randint(1, 1000)
            bot.reply_to(message, "Я задумал число от 1 до 1000ю Попробуй угадать мое число!")
        else:
            bot.reply_to(message, "Я уже загадал число, угадывай!")

    elif game_started:
        if message.text.isdigit():
            number = int(message.text)
            if number > r_number:
                bot.reply_to(message, "Меньше!")
            elif number < r_number:
                bot.reply_to(message, "Больше!")
            elif number == r_number:
                game_started = False
                bot.reply_to(message, f"Поздравляю! Ты угадал мое число {r_number}")
            else:
                bot.reply_to(message, "Попробуй ещё раз, не понимаю тебя")
        else:
            bot.reply_to(message, "Я загадал число, введи число, пожалуйста, чтобы поиграть")
            return
    elif message.text == "вычислить математическое выражение":
        bot.reply_to(message, "Введи математическое выражение, которое нужно посчитать")
        bot.register_next_step_handler(message, calculate)

def calculate(message):
    bot.reply_to(message, f"Ответ: {eval(message.text)}")


bot.infinity_polling()