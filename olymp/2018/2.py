a, b = input().split()
d = len(b) - len(a)
if d < 0:
	d *= -1
	a, b = b, a
c = int(b[:d])
for i in range(len(a)):
	e = int(a[i]) + int(b[d+i])
	if e > 9:
		c = c * 100 + e
	else:
		c = c * 10 + e
print(c)