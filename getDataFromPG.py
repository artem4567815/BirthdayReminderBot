import psycopg2
from config import host, user, password, db_name
import datetime

date = datetime.date.today()
users = []
bedinOfMesssage = "🎉🎉🎉 Празднуем День Рождения: "
lastMessage = ""
def getDataFromDB():
    global lastMessage
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT name, day FROM users;"
            )
            informations = cursor.fetchall()
            for data in informations:
                if str(data[1]) == str(date):
                    users.append(data[0])
            for people in users:
                endOfMessage = '\n' + people
            message = bedinOfMesssage + endOfMessage
            if message != lastMessage:
                lastMessage = message
                return message
            else:
                return ""
    except Exception as _ex:
        print("[INFO] Error", _ex)
    finally:
        if conn:
            conn.close()
