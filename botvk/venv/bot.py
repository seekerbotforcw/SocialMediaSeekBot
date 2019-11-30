import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
token = '50b00e3f0f5ed5fac0e60f4036ab1dbe7204c1eea6a4eac8fae6d85c32c951db1b352b39a460f71f7f20d'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")


#отправка местоположения места пользователю
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            result = vk_session.method("messages.getById", {"message_ids": [event.message_id],
                                                            "group_id": 189348591})
            geo = result['items'][0]['geo']['coordinates']
            latitude, longitude = geo['latitude'], geo['longitude']
            print(latitude, longitude)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id' : time.time()})
    # функция работы с местополжения
def get_geo(latitude, longitude, distance, min_timestamp, max_timestamp, getProfiles):
    get_request =  '/method/photos.search?lat=' + location_latitude
    get_request += '&long=' + location_longitude
    get_request += '&count=100'
    get_request += '&radius=' + distance