import urllib.request
from bs4 import BeautifulSoup
import telebot
import time
import constants
import os


bot = telebot.TeleBot(constants.token)
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

def site(url):
    coll = urllib.request.urlopen(url)
    time.sleep(2)
    return coll.read()

def main():
    
  
    TOKEN = "token"
    PORT = int(os.environ.get('PORT', '5000'))
    updater = Updater(TOKEN)

    parse(site('http://www.kino.kz/cinema.asp?cinemaid=50'))
if __name__ == '__main__':
    main()
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("https://polar-inlet-33421.herokuapp.com/" + TOKEN)
    updater.idle()

