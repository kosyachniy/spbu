import sympy, math

x = sympy.Symbol('x')
a = 0.8
b = 1.3
alpha = 0
beta = sympy.Rational(4, 7)

#f = 5.7 * math.cos(2.5 * x) * math.exp(-4 * x / 7) + 4.4 * math.sin(4.3 * x) * math.exp(2 * x / 7) + 5
f = 5.7 * sympy.cos(2.5 * x) * sympy.exp(-4 * x / 7) + 4.4 * sympy.sin(4.3 * x) * sympy.exp(2 * x / 7) + 5

#print(sympy.integrate(f, (x, a, b)))

def newton(f, a, b, k):
	h = (b - a) / k
	for i in ramge(k):
		start = a + (i - 1) * h
		stop = a * i * h
		center = a + (i - 0.5) * h

		for s in range(2):
			mu[i][s] = 