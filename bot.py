
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

TOKEN = "8326670964:AAHgtWMXzr2dPV66zH6v50QChIWIphrHxRI"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

print(requests.get(url).json())

def start(update, context):
    update.message.reply_text("Салам! Мен группадан да иштейм.")

def echo(update, context):
    chat_id = update.message.chat_id
    update.message.reply_text(f"Chat ID: {chat_id}")
    print("CHAT ID:", chat_id)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()