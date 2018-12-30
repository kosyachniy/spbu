n = int(input())
m = [input().split() for i in range(n)]
m = [int(i[1])/int(i[0]) if i[0]!='0' else 1000000001 for i in m]

a = [0]
for i in range(n):
	if m[i] > m[a[-1]]:
		a.append(i)
o = len(a)

for i in range(1, n-o):
	if m[i] <= m[a[0]]:
		b = [i]
		for j in range(i+1, n):
			if m[j] > m[b[-1]]:
				b.append(j)

		if len(b) > o:
			o = len(b)
			a = b

print(o)
print(*[i+1 for i in a], sep=' ')