from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import time
from threading import Thread

vk = vk_api.VkApi(token="API ТОКЕН ГРУППЫ")

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, ID ГРУППЫ)
stickers = [i for i in range(100)]
photos = ["photo-206086031_457239018", "photo-206086031_457239020", "photo-206086031_457239021"]

while True:
    for event in longpoll.listen():
        while True:
            if event.object.action['type'] == "chat_invite_user":
                vk.method("messages.send", {"peer_id": event.object.peer_id,
                                        "message": 10 *"🚗🚓🚕🛺🚙🚌🚐🚎🚑🚒🚚🚛🚜🚘🚔🚖🚍🦽🦼🛹🚲🛴🛵🏍🏎🚄🚅🚈🚝🚞🚃🚋🚆🚉🚊🚟🚇🚠🚡🚂🚂🚀🚁💺🛬🛫🛫✈🪂🛩🛸🛰⛵🕋🏦💒🗼🏪🏪🏪",
                                        "sticker_id" : random.choice(stickers),
                                        "random_id": 0})

                vk.method("messages.send", {"peer_id": event.object.peer_id,
                                                        "message": 10 *"🚗🚓🚕🛺🚙🚌🚐🚎🚑🚒🚚🚛🚜🚘🚔🚖🚍🦽🦼🛹🚲🛴🛵🏍🏎🚄🚅🚈🚝🚞🚃🚋🚆🚉🚊🚟🚇🚠🚡🚂🚂🚀🚁💺🛬🛫🛫✈🪂🛩🛸🛰⛵🕋🏦💒🗼🏪🏪🏪",
                                                        "attachment" : random.choice(photos),
                                                        "random_id": 0})

            time.sleep(0.5)
            
