a, b = input().split()

d = len(b)
if d < len(a):
	d *= -1
	a, b = b, a

j = 0
for i in a:
