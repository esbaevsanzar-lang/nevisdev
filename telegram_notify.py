import requests


TELEGRAM_TOKEN = "8326670964:AAHgtWMXzr2dPV66zH6v50QChIWIphrHxRI"
CHAT_ID = "-5023367678"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": -5023367678, "text": text}
    requests.post(url, data=data)