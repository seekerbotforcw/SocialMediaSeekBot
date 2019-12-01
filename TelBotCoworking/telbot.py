import telebot
from telebot import types
from math import sin, cos, radians, asin, sqrt

token = "1038002086:AAH7PVaLhrtwjhyf7RmB-VtbREfDLWOzwaw"

bot = telebot.TeleBot(token)

def haversine(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)


along=[59.9139503, 59.9080238]
alat=[30.4490375, 30.3512545]

f=open("db.txt","r+",encoding="utf8")
s=(f.read())
a=s.replace("\n","|").split('|')
f.close()
c=[a[d:d+3] for d in range(0, len(a), 3)]
dist=5

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        answ = haversine(message.location.latitude, message.location.longitude, float(c[0][1]), float(c[0][2]))
        lat=float(c[0][1])
        long=float(c[0][2])
        ind=1
        for i in range(1, len(c), 1):
            if answ <= haversine(message.location.latitude, message.location.longitude, float(c[i][1]), float(c[i][2])):
                answ = answ
            else:
                answ = haversine(message.location.latitude, message.location.longitude, float(c[i][1]), float(c[i][2]))
                lat=float(c[i][1])
                long=float(c[i][2])
                ind=i
        # for i in range(len(along)):
        bot.send_location(message.chat.id, lat, long)
        bot.send_message(message.chat.id, "Расстояние в км до коворкинга "+str(c[ind][0])+" примерно " + str(round(answ,2))+" км")
bot.polling()


