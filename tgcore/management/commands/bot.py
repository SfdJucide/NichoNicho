import logging
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from nicho_nicho.settings import TOKEN, CHAT_ID
from tgcore.management.commands import db


logging.basicConfig(level=logging.INFO)
tg_bot=telebot.TeleBot(TOKEN)


@tg_bot.message_handler(commands=['start'])
def start_message(message):
    db.add_user(message.from_user.id, message.from_user.username)
    markup = InlineKeyboardMarkup()
    item1 = InlineKeyboardButton("Начать", callback_data='start')
    markup.add(item1)	
    tg_bot.send_message(message.chat.id, f"Привет, {message.from_user.username}!\nДобро пожаловать в сообщество nicho nicho! 🙂 ", reply_markup=markup)


@tg_bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "start":
            markup = InlineKeyboardMarkup()
            item1 = InlineKeyboardButton("Каталог", web_app=WebAppInfo(url="https://127.0.0.1:8000/tg/catalog"))
            item2 = InlineKeyboardButton("Связаться с нами", callback_data='help')
            markup.add(item1)	
            markup.add(item2)	
            tg_bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Выберите что вам нужно", reply_markup=markup)
        elif call.data == 'help':
            markup = InlineKeyboardMarkup()
            item1 = InlineKeyboardButton('Оставить отзыв или предложение', web_app=WebAppInfo(url=f"https://127.0.0.1:8000/tg/feedback/?user_id={call.from_user.id}&q=0"))
            item2 = InlineKeyboardButton('Задать вопрос', web_app=WebAppInfo(url=f"https://127.0.0.1:8000/tg/feedback/?user_id={call.from_user.id}&q=1"))
            item3 = InlineKeyboardButton('🏠', callback_data='start')
            markup.add(item1)	
            markup.add(item2)	
            markup.add(item3)	
            tg_bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Выберите что вам нужно", reply_markup=markup)



def send_data(info_msg):
    tg_bot.send_message(chat_id=CHAT_ID, text=info_msg)
