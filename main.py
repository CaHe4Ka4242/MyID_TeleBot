import telebot

bot = telebot.TeleBot('ВАШ_КЛЮЧ') #Здесь вставьте ваш API ключ от @BotFather в телеграмме

#Команда /start

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, Что бы узнать ваш Telegram-ID, напишите команду /MyID')

#Команда /MyID

@bot.message_handler(commands=['MyID', 'айди', 'Айди', 'АЙДИ'])
def ID(message):
    bot.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}.')

#Команда /help

@bot.message_handler(commands=['help'])
def faq(message):
    bot.send_message(message.chat.id, 'Бот может не работать, он на раней стадии разработки и иногда он может тестироваться разработчиком.')

#Команда /command

@bot.message_handler(commands=['command'])
def commandx(message):
    bot.send_message(message.chat.id, 'Команды: /start, /MyID, /help, /command')

bot.infinity_polling()
