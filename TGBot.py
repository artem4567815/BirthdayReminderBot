import telebot
from getDataFromPG import getDataFromDB
from config import token, stikerId
import json
import os

bot = telebot.TeleBot(token=token)
users = []

@bot.message_handler(commands=['start'])
def strat(message):
    user = message.chat.id
    users.append(user)
    with open("clientId.txt", "w") as file:
        json.dump(users, file, indent=1)
    try:
        bot.send_message(user, "success")
    except:
        print("ERROR")

@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    if message.chat.id in users:
        users.remove(message.chat.id)
        with open("clientId.txt", "w") as file:
            json.dump(users, file, indent=1)
    try:
        bot.send_message(message.chat.id, 'Отключили!')
    except:
        print("ERROR")
def sendMessage():
    useres = []
    message = getDataFromDB()
    if os.path.isfile("clientId.txt"):
        with open("clientId.txt", "r") as file:
            useres = json.load(file)
    for user in useres:
        chatId = user
        if message != "":
            try:
                bot.send_message(chatId, message, parse_mode="Markdown")
                bot.send_sticker(chatId, stikerId)
                print("success")
            except:
                print("ERROR")

if __name__ == "__main__":
    bot.polling(none_stop=True)
