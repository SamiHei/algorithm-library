#! /usr/bin/python3


from node import Node
from binary_tree import BinaryTree


def main():

    # This is for testing
    node1 = Node(1)
    tree = BinaryTree(node1)

    tree.add_node_in_order(2)
    tree.add_node_in_order(3)

    tree.add_node_in_order(0)

    tree.add_node_in_order(10)
    tree.add_node_in_order(8)
    tree.add_node_in_orderw(7)

    print(tree.root.right.key)
    print(tree.root.right.right.key)
    print(tree.root.left.key)
    print(tree.root.right.right.right.key)

    print(tree.root.right.right.right.left.key)
    print(tree.root.right.right.right.left.left.key)


if __name__ == "__main__":
    main()
