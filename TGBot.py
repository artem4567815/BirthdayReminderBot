import telebot
from getDataFromPG import getDataFromDB
from config import token, stikerId
import schedule
from threading import Thread
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
    bot.send_message(user, "success")

@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    if message.chat.id in users:
        users.remove(message.chat.id)
    bot.send_message(message.chat.id, 'Отключили!')
def sendMessage():
    message = getDataFromDB()
    for user in users:
        chatId = user
        if message != "":
            bot.send_message(chatId, message)
            bot.send_sticker(chatId, stikerId)
            print("success")


schedule.every(1).day.at("07:00").do(getDataFromDB)
schedule.every(1).day.at("07:00").do(sendMessage)
# schedule.every(1).minute.do(getDataFromDB)
# schedule.every(1).minute.do(sendMessage)
Thread(target=schedule_checker).start()
bot.polling(none_stop=True)
