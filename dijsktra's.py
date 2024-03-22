def dijkstra(graph, source):
    
    # Initialize distances from the source node to all other nodes
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    
    # Keep track of visited nodes
    visited = {}
    
    # Main loop
    while distances:
        # Select the node with the smallest distance
        current_vertex = min(distances, key=distances.get)
        
        # Mark the current node as visited
        visited[current_vertex] = distances[current_vertex]
        del distances[current_vertex]
        
        # Update distances to adjacent nodes
        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue
            new_distance = visited[current_vertex] + weight
            if new_distance < distances.get(neighbor, float('infinity')):
                distances[neighbor] = new_distance
    
    return visited

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
source_node = 'A'
print(dijkstra(graph, source_node))
