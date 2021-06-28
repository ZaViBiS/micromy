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
        old_filename = download(message.text)
        filename = ffmpeg_convert_webm_to_m4a() # new name
        print(filename)
        audio = open('ASMR try not to tingle! (tapping, breathing, licking) *use headphones*.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        os.remove(filename)
        os.remove('.file/' + old_filename)
    except Exception as e:
        logging.error(e)
        os.remove(filename)
        os.remove('.file/' + old_filename)
        



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
