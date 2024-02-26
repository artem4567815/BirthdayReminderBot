import telebot
from getDataFromPG import getDataFromDB
from config import token, stikerId
import schedule
from time import sleep

bot = telebot.TeleBot(token=token)
users = []

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

@bot.message_handler(commands=['start'])
def strat(message):
    user = message.chat.id
    users.append(user)
    try:
        bot.send_message(user, "success")
    except:
        print("ERROR")

@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    if message.chat.id in users:
        users.remove(message.chat.id)
    try:
        bot.send_message(message.chat.id, 'Отключили!')
    except:
        print("ERROR")
def sendMessage():
    message = getDataFromDB()
    for user in users:
        chatId = user
        if message != "":
            try:
                bot.send_message(chatId, message, parse_mode="Markdown")
                bot.send_sticker(chatId, stikerId)
                print("success")
            except:
                print("ERROR")


# schedule.every(1).day.at("07:00").do(sendMessage)
#schedule.every(1).minute.do(sendMessage)
bot.polling(none_stop=True)
