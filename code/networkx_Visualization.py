import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
movies = pd.read_csv('C:\\Users\\malek\\OneDrive\\Documents\\first-term-2025\\algoritm-datamodel\\project\\ml-25m\\ml-25m\\movies.csv')
ratings = pd.read_csv('C:\\Users\\malek\\OneDrive\\Documents\\first-term-2025\\algoritm-datamodel\\project\\ml-25m\\ml-25m\\ratings.csv')

# Create a graph
G = nx.Graph()

# Add movie nodes
for _, row in movies.iterrows():
    G.add_node(f"movie_{row['movieId']}", type='movie', title=row['title'], genres=row['genres'])

# Add user nodes and edges
for _, row in ratings.iterrows():
    user_node = f"user_{row['userId']}"
    movie_node = f"movie_{row['movieId']}"

    if user_node not in G:
        G.add_node(user_node, type='user')

    G.add_edge(user_node, movie_node, weight=row['rating'])

# 1. Number of Nodes
num_nodes = G.number_of_nodes()
print(f"Number of nodes: {num_nodes}")

# 2. Number of Edges
num_edges = G.number_of_edges()
print(f"Number of edges: {num_edges}")

# 3. Connected or Disconnected
if nx.is_connected(G):
    print("The graph is connected.")
else:
    print("The graph is disconnected.")
    num_connected_components = nx.number_connected_components(G)
    print(f"Number of connected components: {num_connected_components}")

# 4. Hub (Node with the highest degree)
hub_node, hub_degree = max(G.degree(), key=lambda x: x[1])
print(f"The hub is: {hub_node} with {hub_degree} connections.")

# 5. Most Active User
user_nodes = [node for node, data in G.nodes(data=True) if data['type'] == 'user']
most_active_user = max(user_nodes, key=lambda user: G.degree[user])
print(f"The most active user is: {most_active_user} with {G.degree[most_active_user]} ratings.")

# 6. Visualization
plt.figure(figsize=(12, 8))

# Position nodes for visualization
pos = nx.spring_layout(G, k=0.15)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=10, node_color='blue', alpha=0.7)

# Highlight hub node (most connected)
nx.draw_networkx_nodes(G, pos, nodelist=[hub_node], node_size=100, node_color='red', label='Hub (Most Popular Movie)')

# Highlight the most active user
nx.draw_networkx_nodes(G, pos, nodelist=[most_active_user], node_size=100, node_color='green', label='Most Active User')

# Draw edges
nx.draw_networkx_edges(G, pos, alpha=0.1)

plt.title("MovieLens 25M - User-Movie Graph")
plt.legend()
plt.show()
