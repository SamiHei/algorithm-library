#! /usr/bin/python3


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def add_node_in_order(self, root, new_node):
        """
        Adds new node with given value (key) to the correct spot in,
        binary tree (as in value order)

        Args:
        root (Node): Root node of the binary tree
        new_node (Node): New node to be added
        """
        if(root.left and root.key >= new_node.key):
            self.add_node_in_order(root.left, new_node)
        elif(root.right and root.key < new_node.key):
            self.add_node_in_order(root.right, new_node)
        elif(root.left is None and root.key >= new_node.key):
            root.left = new_node
        elif(root.right is None and root.key < new_node.key):
            root.right = new_node

    def delete_node(self, root, key, previous_node=None):
        """
        If node which to be deleted is in the left side of the binary tree,
        this function deletes node from the binary tree and sets the deleted
        node's right children (if not None) node to continue from the previous
        node and adds the node's left children to the tree
        using add_node_in_order function

        If node which to be deleted is in the right side of the binary tree,
        this function deletes node from the binary tree and sets the deleted
        node's left children (if not None) node to continue from the previous
        node and adds the node's right children to the tree
        using add_node_in_order function

        Args:
        root (Node): Root node of the binary tree
        key (int): Value of the node which wanted to be deleted from the tree
        previous_node (Node): Previous node of the handled one (default None)
        """
        if(key == root.key):
            if(root.right is not None and key == previous_node.left.key):
                previous_node.left = root.right
                self.add_node_in_order(previous_node.left, root.left)
            elif(root.left is not None and key == previous_node.left.key):
                previous_node.left = root.left
            elif(root.left is not None and key == previous_node.right.key):
                previous_node.right = root.left
                self.add_node_in_order(previous_node.right, root.right)
            else:
                previous_node.right = root.right
        elif(key < root.key and root.left is not None):
            previous_node = root
            print(previous_node.key)
            self.delete_node(root.left, key, previous_node)
        elif(key > root.key and root.right is not None):
            previous_node = root
            print(previous_node.key)
            self.delete_node(root.right, key, previous_node)
        else:
            print("Node doesn't exist on the given tree!")

    def traverse_tree_pre_order(self, root):
        """
        Traverses the tree's key values in pre-order

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
        Traverses the tree's key values in in-order

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
        Traverses the tree's key values in post-order

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
