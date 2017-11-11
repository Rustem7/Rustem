import os
import urllib.request
from bs4 import BeautifulSoup
import telebot
import time
import constants

import requests
from telegram.ext import CommandHandler, Updater
bo = telebot.TeleBot(constants.token)

class Bot:
    def __init__(self, token, debug=False):
        self._token = token
        self._updater = Updater(token)
        self._debug = debug
        
        
        self._init_handlers()
    
    def run(self):
        port = int(os.environ.get('PORT', '5000'))
        self._updater.start_webhook(listen='0.0.0.0', port=port,
                                    url_path=self._token)
        self._updater.bot.set_webhook(os.environ.get("URL") +
                                      self._token)
        self._updater.idle()
    
    def _init_handlers(self):
        self._updater.dispatcher.add_handler(CommandHandler('rate', self._check_rate))
    
    @staticmethod
     
       
        
    
    def _check_rate(bot, update):
        message = update.message
        
        url = "http://www.kino.kz/cinema.asp?cinemaid='+constants.krg"
        
        response = requests.get(url)
        rate = response.json()['bpi']['USD']['rate_float']
        
        text = "Current Bitcoin rate - ${}".format(rate)
        bot.send_message(chat_id=message.chat_id, text=text)
        
        
    @bo.message_handler(commands=['start', 'help'])
    def handle_start(m):
        markup = types.ReplyKeyboardMarkup()
        markup.row('Фильм')
        bot.send_message(m.chat.id, 'Привет',reply_markup=markup)
       
    
    
