import os

from bot import Bot


token = os.environ.get("341519589:AAGsM9G8_0UHiMxRF2uUhXdootK8m086Yqo")

bot = Bot(token)
bot.run()
