from TGBot import sendMessage
import schedule
from time import sleep

schedule.every(1).minute.do(sendMessage)

while True:
    schedule.run_pending()
    sleep(1)


