import urllib.request
from bs4 import BeautifulSoup
import telebot
import constants

from telebot import types

bot = telebot.TeleBot(constants.token)



def site(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    @bot.message_handler(commands=['start', 'help'])
    def handle_start(m):
        markup = types.ReplyKeyboardMarkup()
        markup.row('Фильм')
        bot.send_message(m.chat.id, 'Привет',reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.text == "Фильм":
            lines = []
            soup = BeautifulSoup(html, 'html.parser')
            for s in soup.find_all('div', class_='detail_content'):
                for k in s.find_all('tr'):
                    for b in k.find_all('strong'):
                        z = b.text

                        I='🔴🎥|'
                        lines.append(I+z+'|'+'\n' +'Время сеанса:'+'\n'+'------------------'+'\n')
                    for h in k.find_all('tr',class_='seance_active'):
                        for p in h.findAll('td')[-10:1]:
                            a=p.text[11:-5]
                            lines.append('⏰'+a+ '\n'+'------------------'+'\n')
            bot.send_message(message.chat.id, ''.join(lines))
def main():
    parse(site('http://www.kino.kz/cinema.asp?cinemaid='+constants.krg))
if __name__ == '__main__':
    main()
bot.polling(none_stop=True, interval=10)
