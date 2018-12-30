def fibonacci(n):
	x = 0
	y = 1
	yield 0
	
	if n < 0:
		n *= -1
		t = True
	else:
		t = False
	
	if n:
		yield 1
	
	if n > 1: 
		for i in range(2, n):
			curent = x + y

			if t and i % 2 == 0:
				yield -curent
			else:
				yield curent

			x, y = y, curent
	
for i in fibonacci(int(input())):
	print(i)
