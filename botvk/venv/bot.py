import vk_api
token = '50b00e3f0f5ed5fac0e60f4036ab1dbe7204c1eea6a4eac8fae6d85c32c951db1b352b39a460f71f7f20d'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:


#функция работы с местополжения
def get_geo(latitude, longitude, distance, min_timestamp, max_timestamp, getProfiles):
    get_request =  '/method/photos.search?lat=' + location_latitude
    get_request += '&long=' + location_longitude
    get_request += '&count=100'
    get_request += '&radius=' + distance