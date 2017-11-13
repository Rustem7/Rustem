from flask import Flask, request
import telebot
import os
import urllib.request
from bs4 import BeautifulSoup
import time
import constants



server = Flask(__name__)
token = "341519589:AAGsM9G8_0UHiMxRF2uUhXdootK8m086Yqo"
bot = telebot.TeleBot(token) 
port = int(os.environ.get("PORT", 5000))

coll = urllib.request.urlopen('http://www.kino.kz/cinema.asp?cinemaid=50')
html=coll.read

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://polar-inlet-33421.herokuapp.com/" + token) #ссылку изменил
    return "!", 200

@server.route("/"+ token, methods=['POST'])
def getMessage():
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "POST", 200

@bot.message_handler(content_types=['text'])
#def start(message):
     
 #   bot.send_message(message.chat.id, 'Hi') #вот эта часть кода исполняется два или три раза
   
def handle_text(message):
    if message.text == "Фильм":
        bot.send_message(message.chat.id, '51651')
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
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
server.run(host='0.0.0.0', port=port)


