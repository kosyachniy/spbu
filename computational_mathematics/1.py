from math import factorial, exp, sin

e2 = 3.4 * 10e-7
e3 = 9 * 10e-8

def my_exp(x):
	i = 1
	s = 1
	n = 1

	while True:
		if abs(n) <= e2:
			return s

		n *= x / i
		s += n
		i += 1

def my_sin(x):
	i = 2
	s = x
	n = x

	while True:
		if abs(n) <= e3:
			return s

		n *= (-1) * x ** 2 / (i * (i + 1))
		s += n
		i += 2

my_z = lambda x: (1 + x) ** 0.5 * my_exp(x + 0.5) * my_sin(0.3 * x + 0.7)
z = lambda x: (1 + x) ** 0.5 * exp(x + 0.5) * sin(0.3 * x + 0.7)

for i in range(50, 61):
	z1 = z(i/100)
	z2 = my_z(i/100)

	print(i/100, z1)
	print(i/100, z2)

	print(abs(z2-z1))
	print('-'*100)