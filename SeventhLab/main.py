#Импорт библиотек, config - хранит в себе токен бота, random и datetime для реализации своих команд
import random
import telebot
from telebot import types
import config
from datetime import datetime

#Создание бота с помощью токена
bot = telebot.TeleBot(config.token)

#Пригодится для обработки команды /exercise
hobbies = ["играть", "учить историю", "дописать лабораторные", "посмотреть YouTube", "изучать программирование", "отдохнуть после учебы"]

#Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    #Создание интерактивной клавиатуры в диалоге с ботом
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤲 Хочу")
    btn2 = types.KeyboardButton("/help")
    btn3 = types.KeyboardButton("❓ Кто твой создатель?")
    btn4 = types.KeyboardButton("❓ Как тебя зовут?")
    btn5 = types.KeyboardButton("⏰ Подскажи точное время")
    #Расположение кнопок на клавиатуре, так как мы хотим
    keyboard.add(btn1, btn3, btn4, btn5, btn2)
    bot.send_message(message.chat.id,
                        'Привет, {0.first_name}! Я создан для того, чтобы показывать расписание.'
                        ' С помощью команды /help ты можешь узнать о моих возможностях'.format(message.from_user),
                        reply_markup=keyboard)

#Обработка команды /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,'Я умею перенаправлять тебя на сайт МТУСИ с расписанием - "Хочу"'
                                     '\nТак же могу рассказать о своем создателе - "Кто твой создатель?"'
                                     '\nПопытаюсь ответить как меня зовут - "Как тебя зовут?"'
                                     '\nСкажу точное время - "Подскажи точное время"'
                                     '\nСлучайное число от 1 до 10 - /random'
                                     '\nВ какой ты группе - /group'
                                     '\nЧем тебе заняться - /exercise')

#Обработка команды /random для случайного числа от 1 до 10
@bot.message_handler(commands=['random'])
def start_message(message):
    bot.send_message(message.chat.id, "Твое число: " + str(random.randint(1, 10)))

#Обработка команды /group с целью выяснить в какой группе человек
@bot.message_handler(commands=['group'])
def start_message(message):
    bot.send_message(message.chat.id, "Ты в группе БИН2204")

#Обработка команды /exercise для выбора занятия на досуг
@bot.message_handler(commands=['exercise'])
def start_message(message):
    bot.send_message(message.chat.id, "Ты можешь - " + random.choice(hobbies))

#Обработка всех текстовых сообщений
@bot.message_handler(content_types=['text'])
def answer(message):
    if (message.text.lower() == "хочу" or message.text == "🤲 Хочу"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Сайт МТУСИ, где ты найдешь расписание", url='https://mtuci.ru/')
        markup.add(button1)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и "
                                          "перейди на сайт)".format(message.from_user),
                                          reply_markup=markup)

    elif (message.text.lower() == "кто твой создатель?" or message.text == "❓ Кто твой создатель?"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Страница github моего создателя:", url='https://github.com/danloncer')
        button2 = types.InlineKeyboardButton("Страница VK моего создателя:", url='https://vk.com/danloncer')
        markup.add(button1)
        markup.add(button2)
        bot.send_message(message.chat.id, "Моего создателя зовут Ермолаев Даниил, он студент МТУСИ. "
                                          "Ниже будут ссылки на него",
                         reply_markup=markup)

    elif (message.text.lower() == "как тебя зовут?" or message.text == "❓ Как тебя зовут?"):
        bot.send_message(message.chat.id, "К сожалению, я не знаю своего имени, "
                                          "но обычно меня называют так, как написано в профиле")

    elif (message.text.lower() == "подскажи точное время" or message.text == "⏰ Подскажи точное время"):
        now = datetime.now()
        bot.send_message(message.chat.id, "На данный момент ==== " + now.strftime("%H:%M:%S"))

    else:
        bot.send_message(message.chat.id, "{0.first_name}, прости, я не понимаю, что ты "
                                          "написал или в моем арсенале нет обработки твоих слов!".format(message.from_user))

#Использую для того, чтобы бот не прекращал свою работу
bot.infinity_polling()