#! /usr/bin/python3

from node import Node


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def add_node_in_order(self, key):
        if(self.root.left is None and self.root.key >= key):
            self.root.left = Node(key)
        elif(self.root.right is None and self.root.key < key):
            self.root.right = Node(key)
        elif(self.root.left is not None and self.root.key >= key):
            latest_node = self.root.left
            self._helper_add_node(latest_node, Node(key))
        elif(self.root.right is not None and self.root.key < key):
            latest_node = self.root.right
            self._helper_add_node(latest_node, Node(key))

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
