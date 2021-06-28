import logging
import os

import telebot

from function import *
from config import *


bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.DEBUG)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'send url')

@bot.message_handler(content_types=['text'])
def text(message):
    try:
        trash = download(message.text)
        filename = name_and_rename(trash)
        audio = open(filename, 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        os.remove(filename)
    except Exception as e:
        logging.error(e)
        os.remove(filename)
    


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
