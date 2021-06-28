'''Telegram bot для скачивания аудио и видео с YouTube по ссылке'''
import random
import os
import os.path
import time
import logging

from src import config
import telebot
from pytube import YouTube
from src import converter
from src import remo



bot = telebot.TeleBot(config.TOKEN)
logging.basicConfig(level=logging.DEBUG)
URL = ''
# '[2021/03/10 09:25:43]' -> '[2021-03-10 09-25-43].txt'
FILE_NAME = remo.normal_datetime().replace('/', '-').replace(':', '-') + '.txt'


while remo.internet_connect() == False:
    time.sleep(10)


# запись в лог
remo.logger(FILE_NAME, remo.normal_datetime() + ' internet is available')

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
        message.chat.id,
        text="What format do you need the file?",
        reply_markup=markup)

    global URL
    URL = message.text


# Включается после срабатывания 'download'
# загружает нужный файл, конвертирует в нужный формат и отправляет
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # -- * ^ mp4 ^ * -- #
    if call.data == '2':
        firstRandomName, twoRandomName = random.random()

        outputName = str(random.random()) + '.mp4'
        try:
            bot.send_message(call.message.chat.id, 'Start of download...')

            video = YouTube(URL)
            videoName = str(video.streams[0].title)

            video = video.streams.order_by('resolution').desc(
            ).first().download(fileName=str(firstRandomName))
            videoName = str(remo.removed(videoName)) + '.mp4'

            print(videoName)
            audio = YouTube(URL).streams.filter(
                only_audio=True).desc().first().download(fileName=str(twoRandomName))
            bot.send_message(call.message.chat.id,
                             'Conversion to the desired format...')
            converter.connect(video, audio, outputName)
            os.rename(outputName, videoName)

            old = outputName
            outputName = videoName

            if os.stat(outputName).st_size <= 5e7:

                sendVideoFile = open(outputName, 'rb')
                bot.send_message(call.message.chat.id, 'Sending...')
                bot.send_video(call.message.chat.id, sendVideoFile)
                sendVideoFile.close()

            else:
                bot.send_message(call.message.chat.id,
                                 'The file is too large.')
            os.remove(video)
            os.remove(audio)
            os.remove(outputName)
            os.remove(old + '.webm')
        except:
            bot.send_message(call.message.chat.id,
                             'There was some kind of error.')
    # -- # -- ^ = = ^ -- # -- #

    elif call.data == '1':  # m4a
        name = random.random()
        outputName = str(random.random()) + '.m4a'

        try:
            bot.send_message(call.message.chat.id, 'Start of download...')
            road = YouTube(URL)
            videoName = str(road.streams[0].title)
            road = road.streams.filter(only_audio=True).desc(
            ).last().download(fileName=str(name))
            bot.send_message(call.message.chat.id,
                             'Conversion to the desired format...')
            videoName = str(remo.removed(videoName)) + '.m4a'
            converter.ogg(road, outputName)
            os.rename(outputName, videoName)
            if os.stat(videoName).st_size <= 50000000:
                audio = open(videoName, 'rb')
                bot.send_message(call.message.chat.id, 'Sending...')
                '''
                if call.from_user.first_name == 'неть':
                    bot.send_audio(config.CHAT, audio)
                else:
                    bot.send_audio(call.message.chat.id, audio)
                '''
                bot.send_audio(call.message.chat.id, audio)
                audio.close()
            else:
                bot.send_message(call.message.chat.id,
                                 'The file is too large.')
            os.remove(videoName)
            os.remove(road)

            remo.logger(FILE_NAME, remo.normal_datetime() +
                        ' successfully sent to ' + call.from_user.first_name)

        except:
            bot.send_message(call.message.chat.id,
                             'There was some kind of error.')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        remo.logger(FILE_NAME, remo.normal_datetime() + e)
        time.sleep(15)
