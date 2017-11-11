import os
import telegram
from telegram.ext import *
from telegram import *

TOKEN = os.environ['constans.token']
PORT = int(os.environ['8080'])

bot = telegram.Bot(TOKEN)

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def start(bot, update):
    #update.message.reply_text("hello world")
    #bot.send_message(text="ciao mondo", chat_id = update.message.chat_id)
    button_list = [
                   InlineKeyboardButton("start", callback_data='start'),
                   InlineKeyboardButton("stop", callback_data='stop'),
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(chat_id = update.message.chat_id , text="Benvenuto nuovo utente. Premi start per avviare il conteggio del tempo, mentre premi stop per fermarlo", reply_markup=reply_markup)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def call(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.text))
    
def answerInlineQuery(bot,update):
  print(query)
  print(user_data)


updater = Updater(TOKEN)

updater.bot.set_webhook("https://polar-inlet-33421.herokuapp.com/" + TOKEN)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler( InlineQueryHandler(callback = answerInlineQuery, pass_user_data = True ) )
updater.dispatcher.add_handler(MessageHandler(Filters.text, callback=call))

updater.idle()
