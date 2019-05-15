import re
import time
import matplotlib.pyplot as plt

connections = []

with open('data.txt', 'r') as file:
	for i in file:
		if '<edge' in i:
			id = int(re.search(r'id="[0-9]*"', i).group(0)[4:-1])
			start = int(re.search(r'source="[0-9]*"', i).group(0)[8:-1])
			stop = int(re.search(r'target="[0-9]*"', i).group(0)[8:-1])
			
			# print(id, start, stop)
			connections.append((start, stop))

print('Количество рёбер:', len(connections))

#

vertex_all = set()
vertex_count = []

for i in connections:
	vertex_all |= set(i)
	vertex_count.extend(i)

# print(len(vertex_all))

#

check_connect = {
	i: {
		j: any([i in u and j in u for u in connections]) for j in vertex_all if j != i
	}
for i in vertex_all}

# print(check_connect)

# 

verhR = dict()
for i in vertex_all:
	verhR[i] = vertex_count.count(i)

la = 0

# print(verhR)


#
# print(max(verhR.values()))
rasp = [0 for i in range(max(verhR.values())+1)]
for i in vertex_all:
	# print(verhR[i])
	rasp[verhR[i]] += 1

rasp = [i/len(vertex_all) for i in rasp]

# print(rasp)

x = range(len(rasp))

ax = plt.gca()

ax.bar(x, rasp)
plt.show()


# 
#

for i in verhR:
	la += verhR[i]

print('среднее', la/len(vertex_all))

def check(p, j):
	global check_connect
	return check_connect[p][j]

verhO = dict()
for i in vertex_all:
	verhU = {j: 0 for j in vertex_all}
	verhU[i] = -1
	for j in vertex_all:
		if i != j and check(i, j):
			verhU[j] = 1
	
	# print(verhU)
	# time.sleep(10)
	
	while 0 in verhU.values():
		# print('!!!', i, verhU)
		for j in vertex_all:
			if verhU[j] == 0:
				try:
					verhU[j] = (min([verhU[p] for p in vertex_all if p != j and verhU[p] > 0 and check(p,j)])+1) * (-1)
				except:
					pass
		
		for j in vertex_all:
			if j != i and verhU[j] < 0:
				verhU[j] *= -1



	# for i in connections:



	
	verhU[i] = 0

	print('---'*100)
	print(i,'\n',time.time(),'\n',verhU)
	
	verhO[i] = verhU

	# for j in vertex_all:
	# 	if i in verhO:
	# 		verhO[i] = dict()

# print(verhO)

dl = 0
count = 0

for i in verhO:
	dl += sum(verhO[i].values())
	count += len(verhO) - 1
	verhO[i] = max(verhO[i].values())

r, d = min(verhO.values()), max(verhO.values())

print(r, d)

print('радиусы')
for i in verhO:
	if verhO[i] == r:
		print(i)

print('диаметры')
for i in verhO:
	if verhO[i] == d:
		print(i)

print(dl, count, 'средняя длина', dl/count)