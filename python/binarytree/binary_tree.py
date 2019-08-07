#! /usr/bin/python3

from node import Node


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def add_node_in_order(self, key):
        """
        Adds new node with given value (key) to the correct spot in,
        binary tree (as in value order)

        Args:
        key (int): Value for new node to be added
        """
        if(self.root.left and self.root.key >= key):
            latest_node = self.root.left
            self._helper_add_node(latest_node, Node(key))
        elif(self.root.right and self.root.key < key):
            latest_node = self.root.right
            self._helper_add_node(latest_node, Node(key))
        elif(self.root.left is None and self.root.key >= key):
            self.root.left = Node(key)
        elif(self.root.right is None and self.root.key < key):
            self.root.right = Node(key)

    def _helper_add_node(self, latest_node, node):
        if(latest_node.left is None and latest_node.key >= node.key):
            latest_node.left = node
            return
        elif(latest_node.right is None and latest_node.key < node.key):
            latest_node.right = node
            return
        elif(latest_node.left and latest_node.key >= node.key):
            self._helper_add_node(latest_node.left, node)
        elif(latest_node.right and latest_node.key < node.key):
            self._helper_add_node(latest_node.right, node)

    def print_tree_pre_order(self, root):
        """
        Prints the tree's key values in preorder

        Args:
        root (Node): tree's root node
        """
        node_keys = []
        if root:
            node_keys.append(root.key)
            node_keys = node_keys + self.print_tree_pre_order(root.left)
            node_keys = node_keys + self.print_tree_pre_order(root.right)
        return node_keys
