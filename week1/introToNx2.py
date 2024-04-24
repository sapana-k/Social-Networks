import networkx as nx  # type: ignore
import matplotlib.pyplot as plt
import random

# G = nx.DiGraph() #directed graph
cities = ['Bangalore', 'Delhi', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur']
weights = []
val = 100
while(val<=2000):
    weights.append(val)
    val+=100
# print(weights)

def create_graph(cities, weights, num_edges):
    G = nx.Graph()
    for city in cities:
        G.add_node(city)
    while(G.number_of_edges()<num_edges):  
        c1 = random.choice(list(G.nodes()))
        c2 = random.choice(list(G.nodes()))
        if c1!=c2 and G.has_edge(c1, c2)==0:
            w = random.choice(weights)
            G.add_edge(c1, c2, weight=w)
    return G

def add_random_edge(G, weights):
    c1 = random.choice(list(G.nodes()))
    c2 = random.choice(list(G.nodes()))
    if c1!=c2 and G.has_edge(c1, c2)==0:
        w = random.choice(weights)
        G.add_edge(c1, c2, weight=w)
        

G = create_graph(cities, weights, 10)
u = 'Hyderabad'
v = 'Delhi'
# print("shortest path ", nx.dijkstra_path(G, u, v))
# print("all paths from ",u ," ", nx.single_source_dijkstra_path(G, u))

# try:
#     l = nx.dijkstra_path_length(G, u, v)
    
# except :
#     l = 'infinity'
# print("shortest path distance - ", l)

#x - y for plot
x  = [0]
y = [10000]
for t in range(1, 11): #make random edges 10 times, and watch how the distance decreases from infinity or 10000
    add_random_edge(G, weights)
    x.append(t)
    try:
        l = nx.dijkstra_path_length(G, u, v)
        y.append(l)
        break
    except:
        l = 10000
        y.append(10000) 
        print("no path")

plt.xlabel("Time")
plt.ylabel("Travelling cost/weight/distance between 2 nodes")
plt.plot(x, y)
plt.show()
nx.draw(G, with_labels = 1)
plt.show()

#finds which nodes are connected using nx.has_path(G, u, v)
# for u in G.nodes():
#     for v in G.nodes():
#         print( u, v, nx.has_path(G, u, v)) 

# print("connected?", nx.is_connected(G)) #is graph connected? is every node connected to every other node

#shortest path

# pos = nx.circular_layout(G)
# nx.draw(G, pos, with_labels=1) #graph with nodes and edges
# nx.draw_networkx_edge_labels(G, pos) #edges with weights/costs on it

# plt.show()


