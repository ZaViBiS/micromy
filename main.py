'''Telegram bot для скачивания аудио и видео с YouTube по ссылке'''

from src import config
import telebot
from pytube import YouTube
import random
import os
from src import converter
from src import remo
import os.path
import logger
import time


bot = telebot.TeleBot(config.TOKEN)
URL = ''


# При получении команд 'id' & 'chat' отправляет id чата из которого пришла команда
@bot.message_handler(commands=['id', 'chat'])
def info(message):
    bot.send_message(message.chat.id, message.chat.id)
    print(message.chat.id)


# При запуске бота или получении команы 'start' отправляет стикер
@bot.message_handler(commands=['start'])
def start123(message):
    bot.send_sticker(
        message.chat.id, config.STIKER)


# При получении текста отпровляет меню выбора.
# После того как пользователь сделал выбор присваевает 'URL' текст который отправил пользователь
@bot.message_handler(content_types=['text'])
def download(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text='🎧 audio', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(
        text='📹 video', callback_data=2))
    bot.send_message(
        message.chat.id, text="What format do you need the file?", reply_markup=markup)
    global URL
    URL = message.text


# Включается после срабатывания 'download'
# загружает нужный файл, конвертирует в нужный формат и отправляет
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # -- * ^ mp4 ^ * -- #
    if call.data == '2':
        videon = random.random()
        audion = random.random()
        outputname = str(random.random()) + '.mp4'
        try:
            bot.send_message(call.message.chat.id, 'Start of download...')
            video = YouTube(URL)
            real = str(video.streams[0].title)
            video = video.streams.order_by('resolution').desc(
            ).first().download(filename=str(videon))
            real = str(remo.removed(real)) + '.mp4'
            print(real)
            audio = YouTube(URL).streams.filter(
                only_audio=True).desc().first().download(filename=str(audion))
            bot.send_message(call.message.chat.id,
                             'Conversion to the desired format...')
            converter.connect(video, audio, outputname)
            os.rename(outputname, real)
            old = outputname
            outputname = real
            if os.stat(outputname).st_size <= 50000000:
                video1 = open(outputname, 'rb')
                bot.send_message(call.message.chat.id, 'Sending...')
                bot.send_video(call.message.chat.id, video1)
                video1.close()
            else:
                bot.send_message(call.message.chat.id,
                                 'The file is too large.')
            os.remove(video)
            os.remove(audio)
            os.remove(outputname)
            os.remove(old + '.webm')
        except:
            bot.send_message(call.message.chat.id,
                             'There was some kind of error.')
    # -- # -- ^ = = ^ -- # -- #

    elif call.data == '1':  # m4a
        name = random.random()
        outputname = str(random.random()) + '.m4a'
        try:
            bot.send_message(call.message.chat.id, 'Start of download...')
            road = YouTube(URL)
            real = str(road.streams[0].title)
            road = road.streams.filter(only_audio=True).desc(
            ).last().download(filename=str(name))
            bot.send_message(call.message.chat.id,
                             'Conversion to the desired format...')
            real = str(remo.removed(real)) + '.m4a'
            converter.ogg(road, outputname)
            os.rename(outputname, real)
            if os.stat(real).st_size <= 50000000:
                audio = open(real, 'rb')
                bot.send_message(call.message.chat.id, 'Sending...')
                if call.from_user.first_name == 'ZaViBiS':
                    bot.send_audio(config.CHAT, audio)
                else:
                    bot.send_audio(call.message.chat.id, audio)
                audio.close()
            else:
                bot.send_message(call.message.chat.id,
                                 'The file is too large.')
            os.remove(real)
            os.remove(road)
        except:
            bot.send_message(call.message.chat.id,
                             'There was some kind of error.')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(e)
        time.sleep(15)
