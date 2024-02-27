import psycopg2
from config import host, user, password, db_name
import datetime

date = datetime.date.today()
users = []
bedinOfMesssage = "🎉🎉🎉 Празднуем День Рождения: "
lastMessage = ""
endOfMessage = ""
link = ""
def getDataFromDB():
    global lastMessage, link, endOfMessage, users
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT name, birthday, telegram FROM users WHERE birthday = '{date}';"
            )
            informations = cursor.fetchall()
            for data in informations:
                if {"name": data[0], "tg": data[2]} not in users:
                    users.append({"name": data[0], "tg": data[2]})
                print(users)
            for people in users:
                if people['name'] not in lastMessage:
                    if people['tg'][0] == "@":
                        link = "t.me/" + people['tg'][1::]
                    elif people['tg'][0:5] == "t.me/":
                        link = people['tg']
                    else:
                        link = "t.me/" + people['tg']
                    endOfMessage = endOfMessage + '\n' + people['name'] + " " + link
            if users:
                message = bedinOfMesssage + endOfMessage
                if message != lastMessage:
                    lastMessage = message
                    return message
                else:
                    return ""
            else:
                return ""
    except Exception as _ex:
        print("[INFO] Error", _ex)
    finally:
        if conn:
            conn.close()
