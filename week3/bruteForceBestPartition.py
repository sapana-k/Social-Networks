import networkx as nx
import matplotlib.pyplot as plt
import itertools
def brute(G):
    #aim = divide the graph into 2 partitions
    all_nodes = list(G.nodes())
    n = G.number_of_nodes()
    first_communities = []
    second_communities = []
    for i in range(1, int(n/2) +1):
        combo = [list(x) for x in itertools.combinations(all_nodes, i)]# all possible combos of 2 partitions
        first_communities.extend(combo)
    for i in range(len(first_communities)):
        second_communities.append(list(set(all_nodes) - set(first_communities[i])))
    
    intranet_edges1 = []
    intranet_edges2 = []
    internet_edges = []
    ratios = []
    
    e = G.number_of_edges()
    for i in range(len(first_communities)): #len of first_communities = no. of different combinations of partitions
        intranet_edges1.append(G.subgraph(first_communities[i]).number_of_edges()) #total no. of possible edges in a graph with first_communities[i] no. of nodes
        intranet_edges2.append(G.subgraph(second_communities[i]).number_of_edges()) 
        internet_edges.append(e - intranet_edges1[i] - intranet_edges2[i])
        ratios.append((float)(intranet_edges1[i] + intranet_edges2[i])/internet_edges[i])
    
    maxi = ratios.index(max(ratios))

    print("2 communities - ", first_communities[maxi], " and ", second_communities[maxi])

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
G.add_edge(7, 2)
G.add_edge(7, 3)
G.add_edge(7, 4)
G.add_edge(3, 2)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(5, 8)
G.add_edge(6, 8)
G.add_edge(1, 8)
G.add_edge(1, 6)

brute(G)
nx.draw(G, with_labels = 1)
plt.show()