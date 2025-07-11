# 📘 Program: Binary Tree Implementation in Python
# This program demonstrates how to create and traverse a binary tree

'''
   A binary tree is a tree data structure where each node has at most two children.

'''


# Node class for the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class with traversal methods
class BinaryTree:
    def __init__(self):
        self.root = None

    # Preorder traversal: Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Inorder traversal: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Postorder traversal: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

# Create binary tree manually
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Preorder traversal:")
tree.preorder(tree.root)  # Output: 1 2 4 5 3
print("\nInorder traversal:")
tree.inorder(tree.root)   # Output: 4 2 5 1 3
print("\nPostorder traversal:")
tree.postorder(tree.root) # Output: 4 5 2 3 1

# 🧠 Explanation:
# Binary tree has nodes with at most two children.
# Traversal is used to access all nodes in a specific order.
