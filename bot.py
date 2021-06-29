import logging
import os

import telebot

from function import *
from config import *


bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'send url')

@bot.message_handler(content_types=['text'])
def text(message):
    try:
        download(message.text)
        filename, old_filename = ffmpeg_convert_webm_to_m4a() # new name
        os.remove('file/' + old_filename)
        audio = open(filename, 'rb')
        bot.send_audio(message.chat.id, audio, timeout=60)
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
