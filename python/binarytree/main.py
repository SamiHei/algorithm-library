#! /usr/bin/python3


from node import Node
from binary_tree import BinaryTree


def main():

    # This is for testing
    node6 = Node(6)
    tree = BinaryTree(node6)
    tree.add_node_in_order(4)
    tree.add_node_in_order(2)
    tree.add_node_in_order(1)
    tree.add_node_in_order(3)
    tree.add_node_in_order(5)
    tree.add_node_in_order(7)

    print(tree.root.key)
    print(tree.root.left.key)
    print(tree.root.left.left.key)
    print(tree.root.left.left.left.key)
    print(tree.root.left.left.right.key)
    print(tree.root.left.right.key)
    print(tree.root.right.key)
    print("===================")

    tree.print_tree_pre_order()


if __name__ == "__main__":
    main()
