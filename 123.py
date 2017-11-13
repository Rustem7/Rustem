from flask import Flask, request
import telebot
import os

server = Flask(__name__)
token = "341519589:AAGsM9G8_0UHiMxRF2uUhXdootK8m086Yqo"
bot = telebot.TeleBot(token) 
port = int(os.environ.get("PORT", 5000))

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://polar-inlet-33421.herokuapp.com/" + token) #ссылку изменил
    return "!", 200

@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_messages(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "ok", 200

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, 'Hi') #вот эта часть кода исполняется два или три раза

server.run(host='0.0.0.0', port=port)


