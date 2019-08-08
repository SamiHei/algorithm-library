#! /usr/bin/python3


from node import Node
from binary_tree import BinaryTree


def main():

    # This is for testing
    node10 = Node(10)
    tree = BinaryTree(node10)
    tree.add_node_in_order(node10, 6)
    tree.add_node_in_order(node10, 3)
    tree.add_node_in_order(node10, 8)
    tree.add_node_in_order(node10, 9)
    tree.add_node_in_order(node10, 7)
    tree.add_node_in_order(node10, 1)
    tree.add_node_in_order(node10, 2)
    tree.add_node_in_order(node10, 4)
    tree.add_node_in_order(node10, 5)
    tree.add_node_in_order(node10, 11)

    print(tree.root.left.right.left.key)

    print(tree.traverse_tree_pre_order(node10))

    print(tree.traverse_tree_in_order(node10))

    print(tree.traverse_tree_post_order(node10))


if __name__ == "__main__":
    main()
