from methods import sendMessage
import schedule
from time import sleep

schedule.every(1).day.at("11:40").do(sendMessage)

while True:
    schedule.run_pending()
    sleep(60)


