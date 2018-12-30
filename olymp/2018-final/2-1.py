input()
x = list(map(int, input().split()))

k = 0
for i, o in enumerate(x):
	for j in x[i+1:]:
		k += o>j

print('yneos'[k%2::2])