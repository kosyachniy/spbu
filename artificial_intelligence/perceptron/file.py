from func import *
import codecs

delete('formated')

with codecs.open('data/'+compilation+'/texts.txt', 'r', 'utf8') as file:
	k = 0

	for i in file:
		k += 1
		x = json.loads(i)['name']
		print(x)

		c = [int(j) for j in json.loads(i)['categories'].split()]
		write(c+text(x), name='formated', typ='a')

	print('-----\nВсего текстов: %d' % (k, ))