import telebot
from methods import load_users, save_users
from config import token, stikerId
import json
import os

bot = telebot.TeleBot(token=token)

users = []


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id

    if user not in users:
        users.append(user)

    save_users(users)

    try:
        bot.send_message(user, "Подключено!")
    except:
        print("ERROR")


@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    users = load_users()

    if message.chat.id in users:
        users.remove(message.chat.id)
        save_users(users)

    try:
        bot.send_message(message.chat.id, 'Отключили!')
    except:
        print("ERROR")


if __name__ == "__main__":
    bot.polling(none_stop=True)
