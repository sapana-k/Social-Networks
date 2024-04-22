import networkx as nx
import matplotlib.pyplot as plt

#G = nx.read_edgelist('edgelist format dataset')
#G = nx.read_pajek('pajek format dataset')
#G = nx.read_graphml('edgelist dataset')
#G = nx.read_gexf('edgelist dataset')

def plot_degree_distribution(G):
    all_degrees = nx.degree(G)
    unique_deg = list(set([a[1] for a in all_degrees]))
    count_of_deg = {}
    for a in unique_deg:
        for x in all_degrees:
            if(x[1]==a):
                count_of_deg[a] = count_of_deg.get(a, 0) + 1
    plt.plot(count_of_deg.keys(), count_of_deg.values(), 'yo-')
    plt.title('Degree distribution of Karate Network')
    plt.xlabel('Degrees')
    plt.ylabel('No. of nodes with degree')
    plt.show()
       
G = nx.read_gml('./karate/karate.gml', label='id')
print(G) #prints info of graph

# plot_degree_distribution(G)

#Density = how sparse or dense is graph, no. of edges divided by total possible edges
print("Density = ", nx.density(G))

#Clustering Coefficient = for a node, how many edges are present between its neighbors divided by total possible edges between its neighbors
print("Clustering Coefficient of each node -")
for i in nx.clustering(G).items():
    print(i)

#Average Clustering Coefficient
print("Average Clustering Coefficient = ", nx.average_clustering(G))

#Diameter = shortest path between 2 most distanced nodes
print("Diameter = ", nx.diameter(G))

nx.draw(G, with_labels = 1)
plt.show()
