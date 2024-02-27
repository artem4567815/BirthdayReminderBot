from TGBot import sendMessage
import schedule
from time import sleep

schedule.every(1).minute.do(sendMessage)
#schedule.every(1).day.at("07:00").do(sendMessage)

while True:
    schedule.run_pending()
    sleep(3600)


