def cht(x):
	if len(x) > 1:
		a, b = x[0], cht(x[1:])
		if b == 2: return 2
		c = abs((a + b) % 2)
		if c == abs((a - b) % 2):
			return c
		else:
			return 2
	else:
		return abs(x[0] % 2)

x = list(map(int, input().split()))
print(('YES', 'NO', 'Eta zadacha slishkom sloznaja!!!')[cht(x)])