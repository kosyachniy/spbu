import csv
import math

from func import H as G, conn


def write(name, data):
	with open(name+'.csv', 'w') as file:
		for i in data:
			csv.writer(file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(i)

nodes = list(G.nodes())
conn = {i: set(conn[i]) for i in conn} 

# Common Neighbors

common_neighbours = [['-'] + nodes]

for i in nodes:
    common_neighbours.append([i] + [len(conn[i] & conn[j]) for j in nodes])

write('common_neighbours', common_neighbours)

# Jaccard’s Coefficient

jaccard_similarity = [['-'] + nodes]

for i in nodes:
    jaccard_similarity.append([i] + [len(conn[i] & conn[j]) / len(conn[i] | conn[j]) for j in nodes])

write('jaccard_similarity', jaccard_similarity)

# Adamic/Adar

frequency_common_neighbors = [['-'] + nodes] + [[i] + [0.0 for j in nodes] for i in nodes]

for i in nodes:
    for j in nodes:
        o, u = nodes.index(i) + 1, nodes.index(j) + 1

        if i == j:
           frequency_common_neighbors[o][u] = 1
        else:
            for node in conn[i] & conn[j]:
                frequency_common_neighbors[o][u] += 1/math.log(len(conn[node]))

write('frequency_common_neighbors', frequency_common_neighbors)

# Preferential Attachment

preferential_attachment_similarity = [['-'] + nodes]

for i in nodes:
    preferential_attachment_similarity.append([i] + [len(conn[i]) * len(conn[j]) for j in conn])

write('preferential_attachment_similarity', preferential_attachment_similarity)