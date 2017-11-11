import os
import urllib.request
from bot import Bot


token = os.environ.get("TOKEN")

bot = Bot(token)



bot.run()
