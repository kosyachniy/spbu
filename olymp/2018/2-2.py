a, b = input().split()

d = len(b) - len(a)
if d < 0:
	d *= -1
	a, b = b, a

c = b[:d] + ''.join([str(int(a[i]) + int(b[d+i])) for i in range(len(a))])

print(c)