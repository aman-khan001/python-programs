# 📚 Python Program to Binary Search Tree (BST) Implementation


'''
   A Binary Search Tree (BST) is a binary tree where each node has a value greater than all values in its left subtree and less than all values in its right subtree.
'''


# Node class for BST
class Node:
    # Initializes a node with a value and pointers to left and right children
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST class with methods for insertion, traversal, and searching
class BST:
    # Initializes an empty BST
    def __init__(self):
        self.root = None

    # Inserts a value into the BST
    def insert(self, value):
        # If the tree is empty, create the root node
        if not self.root:
            self.root = Node(value)
        # Otherwise, insert recursively
        else:
            self._insert_recursive(self.root, value)

    # Helper method to insert a value recursively
    def _insert_recursive(self, node, value):
        # If the value is less than the current node's value, go to the left subtree
        if value < node.value:
            if node.left is None:
                # If left child is None, insert the new value here
                node.left = Node(value)
            else:
                # Otherwise, continue searching in the left subtree
                self._insert_recursive(node.left, value)
        # If the value is greater than or equal to the current node's value, go to the right subtree
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Inorder traversal of the BST (left, root, right)
    def inorder(self, node):
        # Perform inorder traversal to get sorted order of elements
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Searches for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to search for a value recursively
    def _search_recursive(self, node, value):
        # If the node is None, the value is not found
        if not node:
            return False
        # If the value matches the current node's value, return True
        if value == node.value:
            return True
        # If the value is less than the current node's value, search in the left subtree
        elif value < node.value:
            return self._search_recursive(node.left, value)
        # If the value is greater than the current node's value, search in the right subtree
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
