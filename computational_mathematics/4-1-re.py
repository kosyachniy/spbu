import sympy

x = sympy.Symbol('x')
a = 0.8
b = 1.3
alpha = 0
beta = sympy.Rational(4, 7)

f = 5.7 * sympy.cos(2.5 * x) * sympy.exp(-4 * x / 7) + 4.4 * sympy.sin(4.3 * x) * sympy.exp(2 * x / 7) + 5
g = f / (((x - a) ** alpha) * ((b - x) ** beta))

print(sympy.integrate(g, (x, a, b)))