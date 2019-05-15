import networkx as nx
import csv

from func import G


# Матрица смежности

nx.to_pandas_adjacency(G).to_csv('contig_matrix.csv')

# Список смежности

conn = {i: [j[1] for j in G.edges() if j[0] == i] for i in G}
contig_list = ((i, *conn[i]) for i in conn)

with open('contig_list.csv', 'w') as file:
	for i in contig_list:
		csv.writer(file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(i)