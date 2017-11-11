import os
import urllib.request
from bot import Bot


token = os.environ.get("TOKEN")

bot = Bot(token)

parse(site('http://www.kino.kz/cinema.asp?cinemaid='+constants.krg))

def site(url):
    coll = urllib.request.urlopen(url)
    time.sleep(2)
    return coll.read()
bot.run()
