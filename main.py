import os
import urllib.request
from bot import Bot


token = os.environ.get("TOKEN")

bot = Bot(token)


def site(url):
    coll = urllib.request.urlopen('http://www.kino.kz/cinema.asp?cinemaid=50')
    time.sleep(2)
    return coll.read()
bot.run()
