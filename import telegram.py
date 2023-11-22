import schedule
import time
from datetime import datetime
import telegram

def send_message(chat_id, text):
    token = "6988074211:AAE9qvTTMcl09hxwwQ5slUlijMDCZBqHcSM"
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=text)

def send_scheduled_message():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # 오후 11시부터 아침 6시까지 메시지 전송 금지
    if 6 <= now.hour < 23:
        print("Sending message at", current_time)
        # 여기에 메시지를 전송하는 코드 추가
        chat_id = "-1002072112022"
        text = "함수 시작후 30분마다 울리는 알람."
        send_message(chat_id, text)

# 30분 간격으로 send_scheduled_message 함수 예약
schedule.every(30).minutes.do(send_scheduled_message)

while True:
    schedule.run_pending()
    time.sleep(1)
