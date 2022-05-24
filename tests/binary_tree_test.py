"""Unit test of singly linked list"""

import unittest
from data_structure_py.binary_tree import BinaryTree, BinaryTreeNode


class TestSinglyLinkedListClass(unittest.TestCase):
    """TestSinglyLinkedListClass"""

    def setUp(self) -> None:
        #         4
        #      /     \
        #    2         6
        #  /   \     /   \
        # 1     3   5     7
        self.test_tree_1 = BinaryTreeNode(4, BinaryTreeNode(2, BinaryTreeNode(
            1), BinaryTreeNode(3)), BinaryTreeNode(6, BinaryTreeNode(5), BinaryTreeNode(7)))
        #         4
        #      /     \
        #    2         6
        #  /             \
        # 1               7
        self.test_tree_2 = BinaryTreeNode(4, BinaryTreeNode(
            2, left_node=BinaryTreeNode(1)), BinaryTreeNode(6, right_node=BinaryTreeNode(7)))
        #         4
        #      /     \
        #    2         6
        #      \     /
        #       3   5
        self.test_tree_3 = BinaryTreeNode(4, BinaryTreeNode(
            2, right_node=BinaryTreeNode(3)), BinaryTreeNode(6, left_node=BinaryTreeNode(5)))

    def test_correctness_of_inorder_traversal(self):
        """Test correctness of inorder traversal"""
        bitree = BinaryTree(self.test_tree_1)
        self.assertEqual(bitree.inorder(), [1, 2, 3, 4, 5, 6, 7])
        bitree = BinaryTree(self.test_tree_2)
        self.assertEqual(bitree.inorder(), [1, 2, 4, 6, 7])
        bitree = BinaryTree(self.test_tree_3)
        self.assertEqual(bitree.inorder(), [2, 3, 4, 5, 6])

    def test_correctness_of_preorder_traversal(self):
        """Test correctness of preorder traversal"""
        bitree = BinaryTree(self.test_tree_1)
        self.assertEqual(bitree.preorder(), [4, 2, 1, 3, 6, 5, 7])
        bitree = BinaryTree(self.test_tree_2)
        self.assertEqual(bitree.preorder(), [4, 2, 1, 6, 7])
        bitree = BinaryTree(self.test_tree_3)
        self.assertEqual(bitree.preorder(), [4, 2, 3, 6, 5])

    def test_correctness_of_postorder_traversal(self):
        """Test correctness of postorder traversal"""
        bitree = BinaryTree(self.test_tree_1)
        self.assertEqual(bitree.postorder(), [1, 3, 2, 5, 7, 6, 4])
        bitree = BinaryTree(self.test_tree_2)
        self.assertEqual(bitree.postorder(), [1, 2, 7, 6, 4])
        bitree = BinaryTree(self.test_tree_3)
        self.assertEqual(bitree.postorder(), [3, 2, 5, 6, 4])

    def test_correctness_of_levelorder_traversal(self):
        """Test correctness of levelorder traversal"""
        bitree = BinaryTree(self.test_tree_1)
        self.assertEqual(bitree.levelorder(), [4, 2, 6, 1, 3, 5, 7])
        bitree = BinaryTree(self.test_tree_2)
        self.assertEqual(bitree.levelorder(), [4, 2, 6, 1, 7])
        bitree = BinaryTree(self.test_tree_3)
        self.assertEqual(bitree.levelorder(), [4, 2, 6, 3, 5])
        