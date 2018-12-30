from math import log

#http://www.apmath.spbu.ru/ru/structure/depts/is/task4-2016.pdf
e = 10e-4

f = lambda x: x * log(x + 1) - 0.5
df = lambda x: (x + 1) * log(x + 1)
x = 1.5

while True:
	d = f(x) / df(x)
	if d < e:
		break

	x -= d

print(x, f(x))