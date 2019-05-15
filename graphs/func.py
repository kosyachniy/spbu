import networkx as nx


# G = nx.DiGraph()
# G.add_nodes_from(['1', '2', '3', '4', '5'])
# G.add_edge('1', '2')
# G.add_edge('2', '4')
# G.add_edge('4', '5')
# G.add_edge('5', '2')
# G.add_edge('1', '3')
# G.add_edge('3', '5')

G = nx.read_gexf('vk-friends-140420515.gexf')