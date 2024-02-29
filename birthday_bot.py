from infrastructure import bot
from methods import load_users, save_users, get_message

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


@bot.message_handler(commands=['birthdays'])
def get_birhdays(message):
    chat_id = message.chat.id
    try:
        message = get_message()
        if not message:
            message = "Сегодня никто не празднует :("
        bot.send_message(chat_id, message)
    except Exception as e:
        print("ERROR:", e)


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
