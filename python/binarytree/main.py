#! /usr/bin/python3


from node import Node
from binary_tree import BinaryTree


def main():

    # This is for testing
    node10 = Node(10)
    tree = BinaryTree(node10)
    tree.add_node_in_order(6)
    tree.add_node_in_order(3)
    tree.add_node_in_order(8)
    tree.add_node_in_order(9)
    tree.add_node_in_order(7)
    tree.add_node_in_order(1)
    tree.add_node_in_order(2)
    tree.add_node_in_order(4)
    tree.add_node_in_order(5)

    print(tree.root.left.right.left.key)

    print(tree.print_tree_pre_order(node10))


if __name__ == "__main__":
    main()
