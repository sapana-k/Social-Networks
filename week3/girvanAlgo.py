import networkx as nx
import matplotlib.pyplot as plt

def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G) #gives dict - key = edge, value = betwenness centrality
    list1 = []
    for x in dict1.items():
        list1.append(x)
    list1.sort(key = lambda x: x[1], reverse=True)
    return list1[0][0] #returns the edge with highest betweenness in tuple form
    
def girvan(G):
    #keep removing edges till 2 components formed
    c = nx.connected_components(G)
    for i in c:
        l = len(i)
    print("no. of connected components ", l)
    while(l==10):
        G.remove_edge(*edge_to_remove(G)) # * used to get values from the returned tuple
        c = nx.connected_components(G)
        for i in c:
            l = len(i)
        print("no. of connected components ", l)
    return c

# G = nx.barbell_graph(5, 0)
G = nx.karate_club_graph()
c = girvan(G)
print("cc", c)
# nx.draw(G, with_labels = 1)
# plt.show()
for i in c:
    print("defe", i)