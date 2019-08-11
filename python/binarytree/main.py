#! /usr/bin/python3


from node import Node
from binary_tree import BinaryTree


def main():

    # This is for testing
    node10 = Node(10)
    tree = BinaryTree(node10)
    tree.add_node_in_order(node10, Node(6))
    tree.add_node_in_order(node10, Node(3))
    tree.add_node_in_order(node10, Node(8))
    tree.add_node_in_order(node10, Node(9))
    tree.add_node_in_order(node10, Node(7))
    tree.add_node_in_order(node10, Node(1))
    tree.add_node_in_order(node10, Node(2))
    tree.add_node_in_order(node10, Node(4))
    tree.add_node_in_order(node10, Node(5))
    tree.add_node_in_order(node10, Node(11))

    print(tree.root.left.right.left.key)

    print(tree.traverse_tree_pre_order(node10))

    print(tree.traverse_tree_in_order(node10))

    print(tree.traverse_tree_post_order(node10))

    tree.delete_node(node10, 6)

    tree.delete_node(node10, 9)

    tree.delete_node(node10, 123)

    print(tree.traverse_tree_pre_order(node10))

    print(tree.traverse_tree_in_order(node10))

    print(tree.traverse_tree_post_order(node10))

    new_node = tree.search_node(node10, 8)
    if(new_node):
        print(new_node.key)
        print(new_node.left.key)
        print(new_node.left.left.right.key)

    new_node = tree.search_node(node10, 9)

if __name__ == "__main__":
    main()
