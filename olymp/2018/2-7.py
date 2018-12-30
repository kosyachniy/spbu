a, b = [list(map(int, i)) for i in input().split()]

d = len(b) < len(a)
if d: a, b = b, a
print(*b[:d], sep='', end='')
del b[:d]

for i in range(len(a)):
	print(a[0] + b[0], end='')
	del a[0]
	del b[0]