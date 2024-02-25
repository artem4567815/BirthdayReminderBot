import telebot
from getDataFromPG import messages, getDataFromDB
from config import chatId, token, stikerId
import schedule
from threading import Thread
from time import sleep

bot = telebot.TeleBot(token=token)


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(3600)


def start():
    for message in messages:
        bot.send_message(chatId, message)
        bot.send_sticker(chatId, stikerId)
        messages.remove(message)
        print("success")


schedule.every(1).day.at("07:00").do(getDataFromDB)
schedule.every(1).day.at("07:00").do(start)

Thread(target=schedule_checker).start()
bot.polling(none_stop=True)
