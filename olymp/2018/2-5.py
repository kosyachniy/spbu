x, y = input().split()
a, b = len(x), len(y)

if a > b:
	a, b = b, a
	x, y = y, x

c = b-a
print(y[:c], end='')
for i in range(a):
	print(int(x[i]) + int(y[c+i]), end='')
print()