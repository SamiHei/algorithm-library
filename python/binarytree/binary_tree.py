#! /usr/bin/python3

from node import Node


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def add_node_in_order(self, root, key):
        """
        Adds new node with given value (key) to the correct spot in,
        binary tree (as in value order)

        Args:
        root (Node): Root node of the binary tree
        key (int): Value for new node to be added
        """
        if(root.left and root.key >= key):
            self.add_node_in_order(root.left, key)
        elif(root.right and root.key < key):
            self.add_node_in_order(root.right, key)
        elif(root.left is None and root.key >= key):
            root.left = Node(key)
        elif(root.right is None and root.key < key):
            root.right = Node(key)

    def traverse_tree_pre_order(self, root):
        """
        Prints the tree's key values in pre-order

        Args:
        root (Node): tree's root node

        Returns:
        Array of node key values in pre-order
        """
        node_keys = []
        if root:
            node_keys.append(root.key)
            node_keys = node_keys + self.traverse_tree_pre_order(root.left)
            node_keys = node_keys + self.traverse_tree_pre_order(root.right)
        return node_keys

    def traverse_tree_in_order(self, root):
        """
        Prints the tree's key values in in-order

        Args:
        root (Node): tree's root node

        Returns:
        Array of node key values in in-order
        """
        node_keys = []
        if root:
            node_keys = node_keys + self.traverse_tree_in_order(root.left)
            node_keys.append(root.key)
            node_keys = node_keys + self.traverse_tree_in_order(root.right)
        return node_keys

    def traverse_tree_post_order(self, root):
        """
        Prints the tree's key values in post-order

        Args:
        root (Node): tree's root node

        Returns:
        Array of node key values in post-order
        """
        node_keys = []
        if root:
            node_keys = node_keys + self.traverse_tree_post_order(root.left)
            node_keys = node_keys + self.traverse_tree_post_order(root.right)
            node_keys.append(root.key)
        return node_keys
