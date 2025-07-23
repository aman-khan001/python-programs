# 📚 Python Program to Graph Representation and Traversal (BFS & DFS)


'''
    A graph is a collection of nodes (vertices) connected by edges.
   It can be directed or undirected, and can have cycles.
   BFS (Breadth-First Search) explores all neighbors at the present depth prior to moving on to nodes at the next depth level.
   DFS (Depth-First Search) explores as far as possible along each branch before backtracking.
'''


from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS (Depth-First Search) implementation
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# BFS (Breadth-First Search) implementation
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    # Start with the initial node
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        #
        if vertex not in visited:
            # Mark the vertex as visited and print it
            print(vertex, end=" ")
            # Add it to the visited set
            visited.add(vertex)
            queue.extend(graph[vertex])

print("DFS traversal:")
dfs(set(), graph, 'A')  # Output: A B D E F C

print("\nBFS traversal:")
bfs(graph, 'A')  # Output: A B C D E F

# 🧠 Explanation:
# Graph is represented using a dictionary where keys are nodes and values are lists of neighbors.
# DFS explores as far as possible before backtracking (uses recursion).
# BFS explores all neighbors level by level using a queue.
