import networkx as nx  # type: ignore
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

G.nodes() #shows all nodes

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(4, 5)
G.add_edge(4, 6)

G.edges() #show all edges
nx.draw(G)
plt.show()

nx.draw(G, with_labels=1)
plt.show()

Z = nx.complete_graph(10) #complete graph on 10 vertices
Z.order() #no. of nodes in graph
Z.size() #no. of edges in graph
H = nx.gnp_random_graph(20, 0.5) #creates a graph with 20 nodes, with edges generated randomly with 0.5 probability
