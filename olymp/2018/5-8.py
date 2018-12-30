n = int(input())
m = [input().split() for i in range(n)]
m = [int(i[1])/int(i[0]) if i[0]!='0' else 1000000001 for i in m]

i = 1
while True:
	if m[i] > m[i-1]:
		a = [i-1]
		break

	i += 1

for i in range(a[0]+1, len(m)):
	if m[i] > m[a[-1]]:
		a.append(i)

l = len(a)

for i in range(a[0]+1, len(m)-l):
	if m[i] < m[a[0]]:
		b = [i]
		for j in range(i+1, len(m)):
			if m[j] > m[b[-1]]:
				b.append(j)

		if len(b) > l:
			l = len(b)
			a = b

print(l)
print(*[i+1 for i in a], sep=' ')