import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':time.time()})

token = '50b00e3f0f5ed5fac0e60f4036ab1dbe7204c1eea6a4eac8fae6d85c32c951db1b352b39a460f71f7f20d'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "Привет":
                write_msg(event.user_id, "Хай")
            elif request == "Пока":
                write_msg(event.user_id, "Пока((")
                break
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")

#def get_geo(latitude, longitude, distance, min_timestamp, max_timestamp, getProfiles):
 #   get_request =  '/method/photos.search?lat=' + location_latitude
  #  get_request += '&long=' + location_longitude
  #  get_request += '&count=100'
  # get_request += '&radius=' + distance