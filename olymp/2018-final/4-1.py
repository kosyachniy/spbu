n = int(input())

from math import factorial
x = lambda n, k: factorial(n) // (factorial(n-k) * factorial(k))

print(x(3, 2))