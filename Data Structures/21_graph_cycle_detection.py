# 📚 Python Program to Cycle Detection in Directed Graph using DFS


'''
    A cycle in a directed graph occurs when there is a path that starts and ends at the same node.
'''


def has_cycle(graph):
    # Initialize visited and recursion stack
    visited = set()
    rec_stack = set()

    # Helper function for DFS
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        # Visit all neighbors
        for neighbor in graph.get(node, []):
            # If the neighbor is not visited, recurse
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

            elif neighbor in rec_stack:
                return True

        # Remove the node from recursion stack before returning
        rec_stack.remove(node)
        return False

    # Check each node in the graph
    # to handle disconnected components
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Example 1: Graph with a cycle
graph_with_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

# Example 2: Graph without a cycle
graph_without_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': []
}

print("Graph with cycle:", has_cycle(graph_with_cycle))       # Output: True
print("Graph without cycle:", has_cycle(graph_without_cycle)) # Output: False

# 🧠 Explanation:
# We use a recursion stack (rec_stack) to track nodes in the current DFS path.
# If a node is revisited in the same path, a cycle exists.
