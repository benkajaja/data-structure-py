"""Unit test of singly linked list"""

import unittest
from data_structure_py.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedListClass(unittest.TestCase):
    """TestSinglyLinkedListClass"""

    def setUp(self) -> None:
        self.test_num = [-1, -2, 0, -3, 4, 3, 2, 1, 0]
        self.test_num_ascending = sorted(self.test_num)
        self.test_num_descending = sorted(self.test_num, reverse=True)

    def test_pop_from_empty_linked_list(self):
        """Pop from empty linked list should raise exception"""
        sll = SinglyLinkedList()
        with self.assertRaises(Exception):
            sll.pop()

    def test_invalid_pop_index(self):
        """Pop linked list with invalid index should raise exception"""
        sll = SinglyLinkedList()
        for val in self.test_num:
            sll.append(val)

        with self.assertRaises(Exception):
            sll.pop(0)
            sll.pop(-1)

        with self.assertRaises(Exception):
            sll.pop(len(self.test_num)+1)

    def test_correctness_of_append_and_pop(self):
        """Test correctness of append and pop"""
        sll = SinglyLinkedList()

        for val in self.test_num:
            sll.append(val)

        self.assertEqual(sll.length, len(self.test_num))

        for val in self.test_num[::-1]:
            self.assertEqual(sll.pop(), val)

        self.assertEqual(sll.length, 0)

    def test_correctness_of_prepend_and_pop(self):
        """Test correctness of prepend and pop"""
        sll = SinglyLinkedList()

        for val in self.test_num:
            sll.prepend(val)

        self.assertEqual(sll.length, len(self.test_num))

        for val in self.test_num:
            self.assertEqual(sll.pop(), val)

        self.assertEqual(sll.length, 0)

    def test_correctness_of_pop_with_specific_index(self):
        """Test correctness of pop with specific index"""
        sll = SinglyLinkedList()

        for val in self.test_num:
            sll.append(val)

        self.assertEqual(sll.pop(1), self.test_num[0])
        self.assertEqual(sll.pop(2), self.test_num[2])
        self.assertEqual(sll.length, len(self.test_num)-2)

    def test_iterator_of_singly_linked_list(self):
        """Test iterator of singly linked list"""
        sll = SinglyLinkedList()

        for val in self.test_num:
            sll.append(val)

        self.assertEqual(sll.length, len(self.test_num))

        for i, node in enumerate(sll):
            self.assertEqual(node.val, self.test_num[i])

        for val in self.test_num:
            sll.append(val)

        self.assertEqual(sll.length, 2*len(self.test_num))

        for i, node in enumerate(sll):
            self.assertEqual(node.val, self.test_num[i % len(self.test_num)])
