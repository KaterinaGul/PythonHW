import telebot
def send_answer(id, question, answer):
    bot.send_message(id, f"{question} \n Ответ: {answer}")

token = "6195946306:AAHMiIO0cOKo7Q1Em7cH42PkMTJhQ5ic4S8"
bot = telebot.TeleBot(token)

data= open("questions.txt", mode = "r", encoding = "utf-8")
questions_list = data.readlines()
data.close()

answered_questions = []

for row in questions_list:
    slit_row = row.split("%%")
    id = slit_row[0]
    question = slit_row[1]
    print(question[:-1])
    answer = input ("Введите ответ: ")
    if answer != "пропустить":
        send_answer(id, question, answer)
        answered_questions.append(row)
    print("___________________________________")

for answer in answered_questions:
    questions_list.remove(answer)

data = open ("questions.txt", mode = "w", encoding = "utf-8")
data.writelines(questions_list)
data.close()