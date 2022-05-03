"""Unit test of doubly linked list"""

import unittest
from data_structure_py.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedListClass(unittest.TestCase):
    """TestDoublyLinkedListClass"""

    def setUp(self) -> None:
        self.test_num = [-1, -2, 0, -3, 4, 3, 2, 1, 0]
        self.test_num_ascending = sorted(self.test_num)
        self.test_num_descending = sorted(self.test_num, reverse=True)

    def test_pop_from_empty_linked_list(self):
        """Pop from empty linked list should raise exception"""
        dll = DoublyLinkedList()
        with self.assertRaises(Exception):
            dll.pop()

    def test_invalid_pop_index(self):
        """Pop linked list with invalid index should raise exception"""
        dll = DoublyLinkedList()
        for val in self.test_num:
            dll.append(val)

        with self.assertRaises(Exception):
            dll.pop(0)
            dll.pop(-1)

        with self.assertRaises(Exception):
            dll.pop(len(self.test_num)+1)

    def test_correctness_of_append_and_pop(self):
        """Test correctness of append and pop"""
        dll = DoublyLinkedList()

        for val in self.test_num:
            dll.append(val)

        self.assertEqual(dll.length, len(self.test_num))

        for val in self.test_num[::-1]:
            self.assertEqual(dll.pop(), val)

        self.assertEqual(dll.length, 0)

    def test_correctness_of_prepend_and_pop(self):
        """Test correctness of prepend and pop"""
        dll = DoublyLinkedList()

        for val in self.test_num:
            dll.prepend(val)

        self.assertEqual(dll.length, len(self.test_num))

        for val in self.test_num:
            self.assertEqual(dll.pop(), val)

        self.assertEqual(dll.length, 0)

    def test_correctness_of_pop_with_specific_index(self):
        """Test correctness of pop with specific index"""
        dll = DoublyLinkedList()

        for val in self.test_num:
            dll.append(val)

        self.assertEqual(dll.pop(1), self.test_num[0])
        self.assertEqual(dll.pop(2), self.test_num[2])
        self.assertEqual(dll.length, len(self.test_num)-2)

    def test_iterator_of_doubly_linked_list(self):
        """Test iterator of doubly linked list"""
        dll = DoublyLinkedList()

        for val in self.test_num:
            dll.append(val)

        self.assertEqual(dll.length, len(self.test_num))

        for i, node in enumerate(dll):
            self.assertEqual(node.val, self.test_num[i])

        for val in self.test_num:
            dll.append(val)

        self.assertEqual(dll.length, 2*len(self.test_num))

        for i, node in enumerate(dll):
            self.assertEqual(node.val, self.test_num[i % len(self.test_num)])

    def test_string_repr_of_doubly_linked_list(self):
        """Test string repr of doubly linked list"""
        dll = DoublyLinkedList()

        self.assertEqual(str(dll), "None")

        for val in self.test_num:
            dll.append(val)

        self.assertEqual(
            str(dll), " -> ".join([str(n) for n in self.test_num]) + " -> None")
