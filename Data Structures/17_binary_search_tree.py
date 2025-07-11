# 📘 Program: Binary Search Tree (BST) Implementation
# This program demonstrates how to insert and search in a BST


'''
   A Binary Search Tree (BST) is a binary tree where each node has a value greater than all values in its left subtree and less than all values in its right subtree.
'''


# Node class for BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST class
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Testing BST
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("Inorder Traversal of BST:")
bst.inorder(bst.root)  # Output: 20 30 40 50 60 70 80

# Searching for values
print("\nSearch 60:", bst.search(60))  # Output: True
print("Search 25:", bst.search(25))  # Output: False

# 🧠 Explanation:
# In BST, left subtree < root < right subtree.
# Insertions and lookups are done recursively based on value.
