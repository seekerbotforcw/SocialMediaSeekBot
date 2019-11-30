import telebot
from telebot import apihelper

PROXY = 'socks5://51.158.160.34:8010' #необходимо постоянно обновлять

apihelper.proxy = {'https': PROXY}
bot=telebot.TeleBot('1038002086:AAH7PVaLhrtwjhyf7RmB-VtbREfDLWOzwaw')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling(none_stop=True, interval=0)