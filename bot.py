import os
import urllib.request
from bs4 import BeautifulSoup
import telebot
import time
import constants

import requests
from telegram.ext import CommandHandler, Updater


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
        self._updater.dispatcher.add_handler(CommandHandler('film', self.handle_text))
        self._updater.dispatcher.add_handler(CommandHandler('start', self.handle_start))
    @staticmethod
     
       
    def handle_text(bot, update):
        message = update.message
        text="652651651"
        bot.send_message(chat_id=message.chat_id, text=text)
    @staticmethod     
    
    def _check_rate(bot, update):
        message = update.message
        
        url1 = "https://api.coindesk.com/v1/bpi/currentprice.json"
        url = "http://www.kino.kz/cinema.asp?cinemaid=50"
        coll = urllib.request.urlopen(url)
        html= coll.read()
        x=html.text
        response = requests.get(url1)
        rate = response.json()['bpi']['USD']['rate_float']
        
        text = "Current Bitcoin rate - "
        bot.send_message(chat_id=message.chat_id, text=x)
        
    @staticmethod   
    def handle_start(bot, update):
        message = update.message
        url = "http://www.kino.kz/cinema.asp?cinemaid=50"
        coll = urllib.request.urlopen(url)
        html= coll.read()
        

        lines = []
        soup = BeautifulSoup(html, 'html.parser')
        for s in soup.find_all('div', class_='detail_content'):
            bot.send_message(chat_id=message.chat_id, text=s)
            for k in s.find_all('tr'):
                for b in k.find_all('strong'):
                    z = b.text
                    I = '🔴🎥|'
                    lines.append(I + z + '|' + '\n' + 'Время сеанса:' + '\n' + '------------------' + '\n')
                for h in k.find_all('tr', class_='seance_active'):

                    for p in h.findAll('td')[-10:1]:
                        a = p.text[11:-5]
                        lines.append('⏰' + a + '\n' + '------------------' + '\n')
                  
                        
        
        text = ''.join(lines)   
        bot.send_message(chat_id=message.chat_id,''.join(lines) )
        
    
       
        
    
    
            
       
    
    
