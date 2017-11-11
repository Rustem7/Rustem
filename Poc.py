import urllib.request
from bs4 import BeautifulSoup
import telebot
import time
import constants

bot = telebot.TeleBot("341519589:AAGsM9G8_0UHiMxRF2uUhXdootK8m086Yqo")
@bot.message_handler(commands=['start', 'help'])
def handle_start(m):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Фильм')
    bot.send_message(m.chat.id, 'Привет',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Фильм":
        bot.send_message(message.chat.id, 'ddddd')




def main():
  # parse(site('http://www.kino.kz/cinema.asp?cinemaid=50'))
  if __name__ == '__main__':
      main()

bot.polling(none_stop=True)
