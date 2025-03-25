import pandas as pd
import networkx as nx

# Load data
movies = pd.read_csv('C:\\Users\\malek\\OneDrive\\Documents\\first-term-2025\\algoritm-datamodel\\project\\ml-25m\\ml-25m\\movies.csv')
ratings = pd.read_csv('C:\\Users\\malek\\OneDrive\\Documents\\first-term-2025\\algoritm-datamodel\\project\\ml-25m\\ml-25m\\ratings.csv')

# Create a graph
G = nx.Graph()

# Add movie nodes
for _, row in movies.iterrows():
    G.add_node(f"movie_{row['movieId']}", title=row['title'], genres=row['genres'])

# Add user nodes and edges
for _, row in ratings.iterrows():
    user_node = f"user_{row['userId']}"
    movie_node = f"movie_{row['movieId']}"
    
    # Add user node if not already present
    if user_node not in G:
        G.add_node(user_node)
        
    # Add edge (user, movie) with rating as weight
    G.add_edge(user_node, movie_node, weight=row['rating'])

print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

# Example Analysis
# Degree of a specific user
user_id = 'user_1'
print(f"User {user_id} has rated {G.degree[user_id]} movies.")

# Find the most connected movies (popular movies)
popular_movies = sorted(G.degree, key=lambda x: x[1], reverse=True)[:10]
print("Top 10 Most Rated Movies:", popular_movies)
