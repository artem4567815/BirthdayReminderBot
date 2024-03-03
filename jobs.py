from methods import sendMessage
import schedule
from time import sleep
from config import when

print(f"Ready to send at {when}")

schedule.every(1).day.at(when).do(sendMessage)

while True:
    schedule.run_pending()
    sleep(30)


