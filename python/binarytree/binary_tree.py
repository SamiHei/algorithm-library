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
        if(self.root.left is not None and self.root.key >= key):
            latest_node = self.root.left
            self._helper_add_node(latest_node, Node(key))
        elif(self.root.right is not None and self.root.key < key):
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
        elif(latest_node.left is not None and latest_node.key >= node.key):
            self._helper_add_node(latest_node.left, node)
        elif(latest_node.right is not None and latest_node.key < node.key):
            self._helper_add_node(latest_node.right, node)

    # TODO continue from here
    def print_tree_pre_order(self):
        print(self.root.key)
        latest_node = self.root
        if(latest_node.left is not None):
            self._pre_order_helper(latest_node.left)
        elif(latest_node.left is None and latest_node.right is not None):
            self._pre_order_helper(latest_node.right)

    def _pre_order_helper(self, latest_node):
        print(latest_node.key)
        if(latest_node.left is not None):
            latest_node = latest_node.left
            self._pre_order_helper(latest_node)
        elif(latest_node.right is not None):
            latest_node = latest_node.right
            self._pre_order_helper(latest_node)
