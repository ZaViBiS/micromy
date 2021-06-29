from config import TOKEN
from telebot import TeleBot
from config import *

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    audio = open('ASMR try not to tingle! (tapping, breathing, licking) *use headphones*.m4a', 'rb')
    bot.send_audio(message.chat.id, audio, timeout=60)
    audio.close()

bot.polling(none_stop=True)