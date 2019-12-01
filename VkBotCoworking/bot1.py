import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import json
from math import radians, cos, sin, asin, sqrt
def haversine(lat1, lon1, lat2, lon2):
    """
    Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
    """

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

lat2 = 59.9350473
lon2 = 30.314854


token = 'ea0d61f9a38612093efd6be2341f5bb423d682186d8f87a7eaee626b885b5790aeddddd2fb61bca40cd46'
vk = vk_api.VkApi(token=token)

keyboard = {
    "one_time": True,
    "buttons": [
        [{
            "action": {
                "type": "location",
                "payload": "{\"button\": \"dict\"}"
            }
        }]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

longpoll = VkLongPoll(vk)

vk_session = vk.get_api()


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': time.time()})
def write_stik(user_id, stickerid):
    vk.method('messages.sendSticker',{'user_id': user_id, 'sticker_id':  stickerid, 'random_id': time.time()})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            r = event.__dict__
            print(vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": 'unanswered'}))
            idd = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": 'unanswered'})
            for id in idd['items']:
                ID_last = id['conversation']['last_message_id']
                break
            print(ID_last)

            if request == '':
                try:
                    if vk.method("messages.getById", {"message_ids": ID_last })["items"][0]["geo"] is not []:
                        print(vk.method("messages.getById", {"message_ids": ID_last })["items"][0]["geo"])
                        coord = vk.method("messages.getById", {"message_ids": ID_last })["items"][0]["geo"]
                        coord = coord['coordinates']
                        print(coord)
                        latitude = coord['latitude']
                        longitude = coord['longitude']
                        print(latitude)
                        print(longitude)
                        distance = round(haversine(latitude,longitude,lat2,lon2), 2)
                        write_msg(event.user_id, "Ближайший " + str(distance) + " km" + '\n' + 'https://www.google.ru/maps/search/' + str(lat2) + '+' + str(lon2))
                except KeyError:
                    write_msg(event.user_id, 'Я не могу это увидеть ;(')
            elif request == "Привет":
                vk.method("messages.send", {"peer_id": event.peer_id, "message": "Новые кнопки", "random_id": 0,
                                                "keyboard": keyboard})
                write_msg(event.user_id, "Хай")
            elif request == "Пока":
                write_msg(event.user_id, "Пока((")
                break
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")



