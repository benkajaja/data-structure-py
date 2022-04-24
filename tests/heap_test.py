"""Unit test of heap"""

import unittest
from data_structure_py.heap import Heap


class TestHeapClass(unittest.TestCase):
    """TestHeapClass"""

    def setUp(self) -> None:
        self.test_num = [-1, -2, 0, -3, 4, 3, 2, 1, 0]
        self.test_num_ascending = sorted(self.test_num)
        self.test_num_descending = sorted(self.test_num, reverse=True)

    def test_pop_from_empty_heap(self):
        """Pop from empty heap should raise exception"""
        heap = Heap()
        with self.assertRaises(Exception):
            heap.pop()

    def test_get_top_of_empty_heap(self):
        """Get top of empty heap should raise exception"""
        heap = Heap()
        with self.assertRaises(Exception):
            heap.get_top()

    def test_correctness_of_min_heap(self):
        """Test correctness of min heap"""
        heap = Heap()
        for i in self.test_num:
            heap.push(i)

        for _, num in enumerate(self.test_num_ascending):
            self.assertEqual(heap.pop(), num)

    def test_correctness_of_max_heap(self):
        """Test correctness of max heap"""
        heap = Heap(is_min_heap=False)
        for i in self.test_num:
            heap.push(i)

        for _, num in enumerate(self.test_num_descending):
            self.assertEqual(heap.pop(), num)
