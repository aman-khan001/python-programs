# 📚 Python Program to Dijkstra's Algorithm for Shortest Path in Weighted Graph

'''
    Dijkstra's algorithm is used to find the shortest path from a source node to all other nodes in a weighted graph.
    It works by maintaining a priority queue of nodes to explore, always expanding the closest node first.
'''

import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    # Main loop
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            # Calculate the distance to the neighbor
            distance = current_distance + weight
            # If the calculated distance is less than the recorded distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Graph represented as adjacency list with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}:")
for node, distance in distances.items():
    print(f"{node}: {distance}")

# 🧠 Explanation:
# Dijkstra's algorithm uses a priority queue to always expand the closest node.
# It finds the shortest distance from the source node to every other node.
# Time complexity: O((V + E) log V) using a min-heap (priority queue).
