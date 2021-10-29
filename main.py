import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser

# create a graph using networkx
G = nx.Graph()
nodes = ["Sports Complex", "Parking Lot", "Siwaka", "Ph.1A", "Ph.1B", "STC", "Phase2", "Phase3", "J1", "Mada"]
# add nodes to your graph
G.add_nodes_from(nodes)
G.nodes()
# create edges to join your nodes to one another
G.add_edge("Sports Complex", "Siwaka", weight='450')
G.add_edge("Siwaka", "Ph.1A", weight='10')
G.add_edge("Siwaka", "Ph.1B", weight='10')
G.add_edge("Ph.1A", "Ph.1B", weight='100')
G.add_edge("Ph.1A", "Mada", weight='850')
G.add_edge("Ph.1B", "STC", weight='112')
G.add_edge("Ph.1B", "Phase2", weight='112')
G.add_edge("STC", "Phase2", weight='50')
G.add_edge("STC", "Parking Lot", weight='250')
G.add_edge("Phase2", "Phase3", weight='500')
G.add_edge("Phase2", "J1", weight='600')
G.add_edge("Phase3", "Parking Lot", weight='350')
G.add_edge("J1", "Mada", weight='200')
G.add_edge("Mada", "Parking Lot", weight='700')

# mapping nodes to x,y coordinates
G.nodes["Sports Complex"]['pos'] = (-4, 2)
G.nodes["Siwaka"]['pos'] = (-2, 2)
G.nodes["Ph.1A"]['pos'] = (0, 2)
G.nodes["Ph.1B"]['pos'] = (0, 0)
G.nodes["STC"]['pos'] = (0, -2)
G.nodes["Phase2"]['pos'] = (2, 0)
G.nodes["Phase3"]['pos'] = (4, -2)
G.nodes["J1"]['pos'] = (4, 0)
G.nodes["Mada"]['pos'] = (6, 0)
G.nodes["Parking Lot"]['pos'] = (4, -6)

# get the position of the nodes
node_pos = nx.get_node_attributes(G, 'pos')
arc_length = nx.get_edge_attributes(G, 'length')

# call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G, "Sports Complex", "Parking Lot")
print(route_bfs.visited)
route_list = route_bfs.visited

# color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list, route_list[1:]))
# color the edges as well
# print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col, connectionstyle="arc3,rad=1")
# nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
