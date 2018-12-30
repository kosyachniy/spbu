n = int(input())
m = [list(map(int, input().split())) for i in range(n)]
m = [i[1]/i[0] if i[0] else 1000000001 for i in m]

a = [[0]]
for i, b in enumerate(m):
	if b < m[a[-1][0]]:
		a.append([i])

	for j in range(len(a)):
		if b > m[a[j][-1]]:
			a[j].append(i)

l = 0
k = 0
for i, b in enumerate(a):
	if l < len(b):
		l = len(b)
		k = i

print(l)
print(*[i+1 for i in a[k]], sep=' ')