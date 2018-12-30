from vector.func import *

categories = formed(('Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация', 'Выражения', 'Наука', 'Рецепты', 'Происшествие', 'Событие', 'Афиша'))
cats = ('Наука', 'Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация', 'Выражения')
subcats = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 0, 8: 0, 9: 2, 10: 2, 11: 6}

def vector(x):
	print(x)
	try:
		y = model.most_similar_to_given(x, categories)
	except:
		try:
			x = model.most_similar_cosmul(positive=x)
			print(x)
			y = model.most_similar_to_given(x[0][0], categories)
		except:
			return 0
		else:
			return subcats[categories.index(y)], model.distance(x[0][0], y)
	else:
		return subcats[categories.index(y)], model.distance(x, y)

if __name__ == '__main__':
	while True:
		x = formed(input().split())

		z = vector(x)
		print('%s (%d%%)' % (cats[z[0]], z[1] * 100) if z else 'По этим данным невозможно определить категорию!')