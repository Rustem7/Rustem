from flask import Flask, request
import telebot
import os
import urllib.request
from bs4 import BeautifulSoup
import time
import constants



server = Flask(__name__)
token = os.environ.get("TOKEN")
bot = telebot.TeleBot(token) 
port = int(os.environ.get("PORT", 5000))

#parse(site('http://www.kino.kz/cinema.asp?cinemaid=50'))

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get("URL") + token) #ссылку изменил
    return "!", 200

@server.route("/"+ token, methods=['POST'])
def getMessage():
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "POST", 200

#@bot.message_handler()
#def start(message):
    
     
 #   bot.send_message(message.chat.id, 'Hi') #вот эта часть кода исполняется два или три раза
   
def parse(html):
    @bot.message_handler(commands=['start', 'help'])
    def handle_start(m):
        markup = telebot.types.ReplyKeyboardMarkup()
        markup.row('Фильм')
        bot.send_message(m.chat.id, 'Привет тебя приветсвует Кино Бот',reply_markup=markup)

    
    
    
    
    
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        
        
        
        print("\n -------")
        print(datetime.now())
        print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                       message.from_user.last_name,
                                                                       str(message.from_user.id),
                                                                       message.text))

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


def site(url):
    coll = urllib.request.urlopen(url)
    time.sleep(2)
    return coll.read()

   
   
if __name__ == '__main__':
    parse(site('http://www.kino.kz/cinema.asp?cinemaid=50'))

    
    
    
    
    
    
    
    
    
    
    
    
server.run(host='0.0.0.0', port=port)


