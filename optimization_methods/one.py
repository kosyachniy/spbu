from math import exp, sqrt

#Метод Дихотомии
def dichotomy(f, a, b, e, d):
	e1 = (b - a) / 2

	if e1 <= e:
		x = (a + b) / 2
		ff = f(x)

		return x, ff
	else:
		x1 = (a + b - d) / 2
		x2 = (a + b + d) / 2

		if f(x1) <= f(x2):
			b = x2
		else:
			a = x1

		return dichotomy(f, a, b, e, d)

#Метод золотого сечения
def golden_ratio(f, a, b, e, x1, x2):
	e1 = (b - a) / 2

	if e1 <= e:
		x = (a + b) / 2
		ff = f(x)

		return x, ff
	else:
		#x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
		#x2 = a + ((sqrt(5) - 1) / 2) * (b - a)

		if f(x1) <= f(x2):
			b = x2 + 0
			x2 = x1 + 0
			x1 = a + ((3 - sqrt(5)) / 2) * (b - a)

		else:
			a = x1 + 0
			x1 = x2 + 0
			x2 = a + ((sqrt(5) - 1) / 2) * (b - a)

		return golden_ratio(f, a, b, e, x1, x2)


if __name__ == '__main__':
	#Данные
	f = lambda x: (219 / 20) / exp(x) + (3 / 2) * x
	a = -2
	b = 7
	e = 0.001
	d = e * 1.5

	print('Метод Дихотомии')
	print('x* ≈ %f\nf* = %f' % dichotomy(f, a, b, e, d))
	print('Метод золотого сечения')
	print('x* ≈ %f\nf* = %f' % golden_ratio(f, a, b, e, a + ((3 - sqrt(5)) / 2) * (b - a), a + ((sqrt(5) - 1) / 2) * (b - a)))