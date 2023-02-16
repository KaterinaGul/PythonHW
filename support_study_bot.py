import telebot

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Здравствуйте! Я бот техподдержки. Введите команду /question , чтобы оставить свой вопрос")
@bot.message_handler(commands=["question"])
def prepare_to_question(message):
    bot.reply_to(message, "Задайте свой вопрос, а я передам его оператору. Убедитесь, что вопрос написан одним сообщением")
    bot.register_next_step_handler(message, write_question)

def write_question(message):
    data = open ("questions.txt", "a", encoding = "utf-8")
    data.write(f" {message.from_user.id}%%{message.from_user.first_name} {message.from_user.last_name}: {message.text} \n" )
    data.close()
    bot.reply_to(message, "Ваш вопрос отправлен оператору. Среднее время ожидания ответа: 1 час. Спасибо за обращение!")

bot.infinity_polling()
