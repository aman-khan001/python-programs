# 📚 Python Program to Shortest Path in Unweighted Graph using BFS


'''
    In an unweighted graph, the shortest path can be found using Breadth-First Search (BFS).
'''


from collections import deque

# Function to find the shortest path using BFS
def bfs_shortest_path(graph, start, goal):
    # Initialize visited set and queue
    visited = set()
    queue = deque([[start]])

    # If start is the goal, return immediately
    if start == goal:
        return [start]

    # Loop until the queue is empty
    while queue:
        path = queue.popleft()
        node = path[-1]

        # If the node has not been visited
        if node not in visited:
            # Visit all neighbors of the current node
            for neighbor in graph.get(node, []):
                
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path

            visited.add(node)
    return None

# Sample graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Finding shortest path
start_node = 'A'
goal_node = 'F'
shortest_path = bfs_shortest_path(graph, start_node, goal_node)
print(f"Shortest path from {start_node} to {goal_node}: {shortest_path}")

# 🧠 Explanation:
# BFS explores the graph level by level, ensuring the shortest path in an unweighted graph.
# We track paths explicitly in the queue and return as soon as we reach the goal.
