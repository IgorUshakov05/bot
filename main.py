#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types

TOKEN = '6286392838:AAEbculwlD7DSOwD0cIDJiJjfe_xnKX-P4k'
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name  # Получаем имя пользователя
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Нумерология')
    button2 = types.KeyboardButton('Нутрициология')
    button3 = types.KeyboardButton('Траволечение')
    markup.add(button1, button2, button3)

    welcome_message = "Добро пожаловать, {}! 🌟\nЯ здесь, чтобы поделиться знаниями о <b>нумерологии</b>, <b>нутрициологии</b> и <b>траволечении</b>.\nВыбери интересующее направление и вперед к новым знаниям! 💪✨".format(
        user_name)
    bot.reply_to(message, welcome_message, reply_markup=markup, parse_mode='HTML')


@bot.message_handler(func=lambda message: True)
def process_message(message):
    if message.text == 'Нумерология':
        bot.reply_to(message, "Присоединяйся к нашему курсу по 👉<a href='https://ihclick.ru/?p=253394&o=277936&idp=124458'>нумерологии</a>👈", parse_mode='HTML')
        bot.send_message(message.chat.id,"🔢💫 <b>Отличный выбор!</b> 💫🔢\n\nВыбрав этот курс, вы открываете дверь в мир <b>нумерологии</b>, где числа раскроют перед вами свои тайны. \n\n🚀 <b>Погрузитесь</b> в увлекательное путешествие и расширьте свои знания о себе и окружающем мире! 🌟🌎",
                         parse_mode='HTML')

    elif message.text == 'Нутрициология':
        bot.reply_to(message, "Присоединяйся к нашему курсу по 👉<a href='https://ihclick.ru/?p=288387&o=288781&idp=124458'>нутрициологии</a>👈", parse_mode='HTML')
        bot.send_message(message.chat.id,"🍎🥦<b>Великолепный выбор!</b> 🌱🍇\n\nДанный курс предлагает глубокие знания в области <b>нутрициологии</b>. \n\n💡 <b>Вы узнаете</b>, как правильное питание и выбор продуктов влияют на ваше здоровье и благополучие. 🥗💪 \n\n👩‍🍳 Приготовьтесь к открытию новых вкусов и пользы для организма! 🌿🌟",
                         parse_mode='HTML')

    elif message.text == 'Траволечение':
        bot.reply_to(message, "Присоединяйся к нашему курсу по 👉<a href='https://ihclick.ru/?p=276326&o=298346&idp=124458'>траволечению</a>👈", parse_mode='HTML')
        bot.send_message(message.chat.id, "🌿🌱 <b>Отличный выбор!</b> 🌱🌿\n\nДанный курс приглашает вас в мир <b>траволечения</b>, где вы откроете для себя силу природы. \n\n💫 <b>Узнайте</b> о лечебных свойствах различных трав и растений, их использовании в народной медицине и создайте свой собственный набор лекарственных трав! 🌼💚",
                         parse_mode='HTML')

    else:
        bot.reply_to(message, "Я не понимаю. Выбери одно из предложений!")


bot.polling()
