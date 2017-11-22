import telebot
import random
from os import environ
from constants import *

bot = telebot.TeleBot(token)
print(bot.get_me())

def log(message,answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))


@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = "Мои возможности ограничены. Sorry!"
    log(message, answer)
    bot.send_message(message.chat.id, answer )

@bot.message_handler(commands=['start'])
def handle_text(message):
    answer = "Hello! You are welcome!"
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['settings'])
def handle_text(message):
    answer = "Тут пусто)"
    log(message, answer)
    bot.send_message(message.chat.id,answer )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text=='стикер':
        answer = stickers[random.randint(0, len(stickers))]
        bot.send_sticker(message.from_user.id, answer)
    else:
        answer = message.text
        log(message, answer)
        bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['sticker'])
def handle_text(message):
    answer = stickers[random.randint(0,len(stickers))]
    bot.send_sticker(message.from_user.id, answer)
    log(message, answer)


if __name__ == '__main__':
    application.listen(environ["PORT"])
    bot.polling(none_stop=True)
