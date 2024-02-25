import psycopg2
from config import host, user, password, db_name
import datetime

date = datetime.date.today()
messages = []


def getDataFromDB():
    global messages
    try:
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT name, day FROM users;"
            )
            informations = cursor.fetchall()
            for data in informations:
                if str(data[1]) == str(date):
                    messages.append(f"🎉🎉🎉 Празднуем День Рождения: \n {data[0]} \n")
    except Exception as _ex:
        print("[INFO] Error", _ex)
    finally:
        if conn:
            conn.close()
            print("closed")