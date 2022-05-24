"""Implementation of binary tree.

  Typical usage example:
    root = BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3))
    bitree = BinaryTree(root)
    bitree.inorder()
    bitree.preorder()
    bitree.postorder()
    bitree.levelorder()
"""


class BinaryTreeNode:
    """BinaryTreeNode class

    Attributes:
        val: The value of this node
        left_node: The object of left node
        right_node: The object of right node
    """

    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node


class BinaryTree:
    """Binary class

    Attributes:
        root: The root node of binaryTree

    Methods:
        inorder()
        preorder()
        postorder()
        levelorder()
    """

    def __init__(self, root: BinaryTreeNode = None) -> None:
        self.root = root

    def inorder(self) -> list[int]:
        """Iterative inorder traversal"""
        res = []
        cur = self.root
        stack = []

        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left_node
            elif stack:
                node = stack.pop()
                res.append(node.val)
                cur = node.right_node
            else:
                break

        return res

    def preorder(self) -> list[int]:
        """Iterative preorder traversal"""
        res = []
        cur = self.root
        stack = []

        while True:
            if cur is not None:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left_node
            elif stack:
                node = stack.pop()
                cur = node.right_node
            else:
                break

        return res

    def postorder(self) -> list[int]:
        """Iterative postorder traversal"""
        res = []
        stack = [self.root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.left_node is not None:
                stack.append(cur.left_node)

            if cur.right_node is not None:
                stack.append(cur.right_node)

        res.reverse()

        return res

    def levelorder(self) -> list[int]:
        """levelorder traversal"""
        if self.root is None:
            return ""

        res = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)

            if node.left_node:
                queue.append(node.left_node)

            if node.right_node:
                queue.append(node.right_node)

        return res
