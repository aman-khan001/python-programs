# 📘 Program: Shortest Path in Unweighted Graph using BFS
# This program finds the shortest path from a source to destination using BFS


'''
    In an unweighted graph, the shortest path can be found using Breadth-First Search (BFS).
'''


from collections import deque

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
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
