import networkx as nx

# Create the graph object
G = nx.Graph()

# Add nodes
G.add_nodes_from(['New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX', 'Phoenix, AZ',
                  'Cleveland, OH', 'Indianapolis, IN', 'Denver, CO', 'Las Vegas, NV', 'Albuquerque, NM',
                  'Kansas City, MO', 'Oklahoma City, OK', 'Dallas, TX', 'Austin, TX',
                  'El Paso, TX', 'Tucson, AZ', 'Flagstaff, AZ', 'Santa Fe, NM', 'Colorado Springs, CO',
                  'Grand Canyon National Park, AZ'])

# Add edges with distances
G.add_edge('New York, NY', 'Cleveland, OH', weight=400)
G.add_edge('Cleveland, OH', 'Chicago, IL', weight=340)
G.add_edge('Chicago, IL', 'Kansas City, MO', weight=500)
G.add_edge('Kansas City, MO', 'Denver, CO', weight=600)
G.add_edge('Denver, CO', 'Grand Canyon National Park, AZ', weight=700)
G.add_edge('Grand Canyon National Park, AZ', 'Flagstaff, AZ', weight=145)
G.add_edge('Flagstaff, AZ', 'Phoenix, AZ', weight=150)
G.add_edge('New York, NY', 'Indianapolis, IN', weight=680)
G.add_edge('Indianapolis, IN', 'Kansas City, MO', weight=550)
G.add_edge('Kansas City, MO', 'Oklahoma City, OK', weight=350)
G.add_edge('Oklahoma City, OK', 'Albuquerque, NM', weight=500)
G.add_edge('Albuquerque, NM', 'Flagstaff, AZ', weight=400)
G.add_edge('Phoenix, AZ', 'Tucson, AZ', weight=120)
G.add_edge('Tucson, AZ', 'El Paso, TX', weight=320)
G.add_edge('El Paso, TX', 'Santa Fe, NM', weight=480)
G.add_edge('Santa Fe, NM', 'Colorado Springs, CO', weight=470)
G.add_edge('Colorado Springs, CO', 'Denver, CO', weight=100)
G.add_edge('Houston, TX', 'Austin, TX', weight=160)
G.add_edge('Austin, TX', 'Dallas, TX', weight=195)
G.add_edge('Dallas, TX', 'Oklahoma City, OK', weight=210)
G.add_edge('Oklahoma City, OK', 'Kansas City, MO', weight=350)
G.add_edge('Las Vegas, NV', 'Flagstaff, AZ', weight=300)
G.add_edge('Las Vegas, NV', 'Los Angeles, CA', weight=270)

import matplotlib.pyplot as plt

# set positions for the nodes (optional)
pos = nx.spring_layout(G)

# draw the nodes and edges
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)

# draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# draw node labels
node_labels = {node: node.split(',')[0] for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

# show the plot
plt.axis('off')
plt.show()
