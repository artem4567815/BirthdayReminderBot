import psycopg2
from config import host, user, password, db_name, stickerId
from infrastructure import bot
import json
import datetime

beginOfMesssage = "🎉🎉🎉 Празднуем День Рождения: "
query = """SELECT DISTINCT id, name, telegram FROM users WHERE
    EXTRACT(MONTH FROM birthday) = EXTRACT(MONTH FROM TIMESTAMP %s) AND
    EXTRACT(DAY FROM birthday) = EXTRACT(DAY FROM TIMESTAMP %s);"""


def load_users():
    try:
        with open('users.json') as file:
            return json.load(file)
    except:
        return []


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=1)


def sendMessage():
    print("Running...")
    message = get_message()

    print(message)

    if message != "":
        for user in load_users():
            print(user)
            try:
                bot.send_message(user, message, parse_mode="Markdown")
                bot.send_sticker(user, stickerId)
                print("success")
            except:
                print("ERROR")


def get_postgres_connection():
    return psycopg2.connect(host=host, user=user, password=password, database=db_name)


def user_to_dict(data):
    return {"name": data[1], "tg": data[2]}


def get_tg_link(person):
    if not person['tg']:
        return None

    if person['tg'][0] == "@":
        link = "t.me/" + person['tg'][1::]
    elif person['tg'][0:5] == "t.me/":
        link = person['tg']
    else:
        link = "t.me/" + person['tg']

    return link


def get_message():
    date = datetime.date.today()
    message = ""
    conn = None

    try:
        conn = get_postgres_connection()

        with conn.cursor() as cursor:
            cursor.execute(query, [date, date])
            birthday_users = list(map(user_to_dict, cursor.fetchall()))

            for person in birthday_users:
                tg_link = get_tg_link(person)
                message += '\n' + person['name']

                if tg_link:
                    message += " " + tg_link

        if message:
            return beginOfMesssage + message
    except Exception as _ex:
        print("[INFO] Error", _ex)
    finally:
        if conn:
            conn.close()
