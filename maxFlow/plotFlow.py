import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from fractions import Fraction

def plot_graph_from_matrix(adj_matrix, source, sink):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes and edges to the graph
    for i, row in enumerate(adj_matrix):
        for j, capacity in enumerate(row):
            if capacity > 0:
                G.add_edge(i, j, capacity=capacity)

    # Use BFS to determine the levels of each node from the source
    levels = {source: 0}
    queue = [source]
    while queue:
        current = queue.pop(0)
        current_level = levels[current]
        for neighbor in G.neighbors(current):
            if neighbor not in levels:  # Neighbor has not been visited
                levels[neighbor] = current_level + 1
                queue.append(neighbor)

    # Calculate positions based on levels
    pos = {}
    vertical_locations = {}
    for node, level in levels.items():
        if level not in vertical_locations:
            vertical_locations[level] = []
        vertical_locations[level].append(node)

    # Place nodes at each level, centered and evenly spaced
    for level, nodes in vertical_locations.items():
        x_positions = np.linspace(0, 1, len(nodes)+2)[1:-1]  # Skip first and last to center nodes
        for i, node in enumerate(nodes):
            pos[node] = (x_positions[i], -level)

    # Ensure the sink is at the bottom level if it's not already placed
    if sink not in pos:
        max_level = max(levels.values()) + 1
        pos[sink] = (0.5, -max_level)  # Center sink below the last level

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='white',edgecolors='black', node_size=2000, font_size=15, font_weight='bold')
    
    # Draw edge labels (capacities)
    edge_labels = {(i, j): w['capacity'] for i, j, w in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Display the plot
    plt.title("Flow Network Graph")
    plt.show()
    
def plot_graph_from_matrix_string(adj_matrix, source, sink):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes and edges to the graph
    for i, row in enumerate(adj_matrix):
        for j, capacity in enumerate(row):
            if capacity != '0':  # Ensure the capacity is not '0', indicating an edge exists
                G.add_edge(i, j, capacity=capacity)  # Use the string fraction as the label

    # Use BFS to determine the levels of each node from the source
    levels = {source: 0}
    queue = [source]
    while queue:
        current = queue.pop(0)
        current_level = levels[current]
        for neighbor in G.neighbors(current):
            if neighbor not in levels:  # Neighbor has not been visited
                levels[neighbor] = current_level + 1
                queue.append(neighbor)

    # Calculate positions based on levels
    pos = {}
    vertical_locations = {}
    for node, level in levels.items():
        if level not in vertical_locations:
            vertical_locations[level] = []
        vertical_locations[level].append(node)

    # Place nodes at each level, centered and evenly spaced
    for level, nodes in vertical_locations.items():
        x_positions = np.linspace(0, 1, len(nodes)+2)[1:-1]  # Skip first and last to center nodes
        for i, node in enumerate(nodes):
            pos[node] = (x_positions[i], -level)

    # Ensure the sink is at the bottom level if it's not already placed
    if sink not in pos:
        max_level = max(levels.values()) + 1
        pos[sink] = (0.5, -max_level)  # Center sink below the last level

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='white', edgecolors='black', node_size=2000, font_size=15, font_weight='bold')
    
    # Draw edge labels with adjusted positions
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    for (u, v), label in edge_labels.items():
        label_pos = (pos[u][0] * 0.6 + pos[v][0] * 0.4, pos[u][1] * 0.6 + pos[v][1] * 0.4)  # Adjust label position
        plt.text(label_pos[0], label_pos[1], label, size=12, color='black', ha='center', va='center',bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))

    # Display the plot
    plt.title("Flow Network Graph")
    plt.axis('off')  # Turn off the axis for a cleaner look
    plt.show()
    
def plot_graph_from_matrix_string2(adj_matrix, source, sink):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add nodes and edges to the graph
    for i, row in enumerate(adj_matrix):
        for j, capacity in enumerate(row):
            if capacity != '0':  # Ensure the capacity is not '0', indicating an edge exists
                G.add_edge(i, j, capacity=capacity)  # Use the string fraction as the label

    # Use BFS to determine the levels of each node from the source
    levels = {source: 0}
    queue = [source]
    while queue:
        current = queue.pop(0)
        current_level = levels[current]
        for neighbor in G.neighbors(current):
            if neighbor not in levels:  # Neighbor has not been visited
                levels[neighbor] = current_level + 1
                queue.append(neighbor)

    # Calculate positions based on levels
    pos = {}
    vertical_locations = {}
    for node, level in levels.items():
        if level not in vertical_locations:
            vertical_locations[level] = []
        vertical_locations[level].append(node)

    # Place nodes at each level, centered and evenly spaced
    for level, nodes in vertical_locations.items():
        x_positions = np.linspace(0, 1, len(nodes)+2)[1:-1]  # Skip first and last to center nodes
        for i, node in enumerate(nodes):
            pos[node] = (x_positions[i], -level)

    # Ensure the sink is at the bottom level if it's not already placed
    if sink not in pos:
        max_level = max(levels.values()) + 1
        pos[sink] = (0.5, -max_level)  # Center sink below the last level

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='white', edgecolors='black', node_size=2000, font_size=15, font_weight='bold')
    
   
    # Draw edge labels (capacities are now fractions)
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Display the plot
    plt.title("Flow Network Graph")
    plt.axis('off')  # Turn off the axis for a cleaner look
    plt.show()