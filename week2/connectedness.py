import networkx as nx
import matplotlib.pyplot as plt
import random

import numpy
   
#create a graph and add edges till its connected
def create(n):
    #input = no. of nodes
    #output = no. of edges required to be just connected
    G = nx.Graph()
    G.add_nodes_from(range(n))
    while(nx.is_connected(G)==False):
        v1 = random.choice(list(G.nodes()))
        v2 = random.choice(list(G.nodes()))
        if v1!=v2:
            G.add_edge(v1, v2)
    # nx.draw(G)
    # plt.show()
    return G.number_of_edges()
    
def plot_till_connectivity():
    x = []
    y = []
    i = 10
    x1 = []
    y1 = []
    while(i<=200):
        x.append(i)
        avg_edges = 0
        for u in range(4):
            avg_edges+=create(i)
        y.append(avg_edges/4)
        x1.append(i)
        y1.append(i*numpy.log(i)/2.0)
        i+=10
    
    plt.xlabel('no. of nodes')
    plt.ylabel('no. of edges till connectivity')
    plt.plot(x, y)
    
    plt.plot(x1, y1)
    plt.show()
plot_till_connectivity()
