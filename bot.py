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
        file = download(message.text)
        if file[1] != 'm4a':
            filename, old_filename = ffmpeg_convert_webm_to_m4a(file[0]) # new name
            os.remove('file/' + old_filename)
        else:
            filename = 'file/' + file[0] + '.m4a'
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
