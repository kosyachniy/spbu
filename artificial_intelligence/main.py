from perceptron.decide import decide
from vector.main import vector

import time, json

with open('data/set.txt', 'r') as file:
	cats = json.loads(file.read())['categories']

#ВКонтакте
import vk_api

with open('data/keys.txt', 'r') as file:
	vk = vk_api.VkApi(token=json.loads(file.read())['token'])
#vk.auth()

send = lambda user, cont: vk.method('messages.send', {'user_id':user, 'message':cont})
readvk = lambda: [[i['user_id'], i['body']] for i in vk.method('messages.get')['items'] if not i['read_state']][::-1]

pretty = lambda x: '%s (%d%%)' % (cats[x[0]], x[1] * 100 if x[1] < 1 else 99) if x else 'По этим данным невозможно определить категорию!'

while True:
	try:
		for i in readvk():
			send(i[0], decide(i[1]))
			z2 = pretty(vector(i[1]))
			if z2: send(i[1], 'Google: ' + z2)
		time.sleep(2)
	except:
		time.sleep(5)
		#vk.auth()