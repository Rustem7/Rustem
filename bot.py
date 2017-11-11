import os
import urllib.request
from bs4 import BeautifulSoup
import telebot
import time
import constants

import requests
from telegram.ext import CommandHandler, Updater


class Bot:
    parse(site('http://www.kino.kz/cinema.asp?cinemaid='+constants.krg))
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
        
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        
        response = requests.get(url)
        rate = response.json()['bpi']['USD']['rate_float']
        
        text = "Current Bitcoin rate - ${}".format(rate)
        bot.send_message(chat_id=message.chat_id, text=text)
        
    def site(url):
        coll = urllib.request.urlopen(url)
        time.sleep(2)
        return coll.read()
    
    def parse(html):
        @bot.message_handler(content_types=['text'])
        def handle_text(message):
            if message.text == "Фильм":
                lines = []
                soup = BeautifulSoup(html, 'html.parser')
                for s in soup.find_all('div', class_='detail_content'):
                    for k in s.find_all('tr'):
                        for b in k.find_all('strong'):
                            z = b.text
                            I = '🔴🎥|'
                            lines.append(I + z + '|' + '\n' + 'Время сеанса:' + '\n' + '------------------' + '\n')
                        for h in k.find_all('tr', class_='seance_active'):
                            for p in h.findAll('td')[-10:1]:
                                a = p.text[11:-5]
                                lines.append('⏰' + a + '\n' + '------------------' + '\n')
                                
                 bot.send_message(message.chat.id, ''.join(lines))
