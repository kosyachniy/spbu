k = int(input())

def t(n, i):
	if n>1:
		t(n-1, i+'0')
		t(n-1, i+'1')
	else:
		print(i)

t(k, '0')
t(k, '1')