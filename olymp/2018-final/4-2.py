n = int(input())

def bi(m, s=0, j=1, k=0):
	s += j
	j += 1

	if s <= m:
		bi(m, s, j, k)
	else:
		print(m, s, j, k)

bi(n) #print(s)