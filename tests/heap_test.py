import unittest
from data_structure_py.heap import heap


class TestHeapClass(unittest.TestCase):

    def setUp(self) -> None:
        self.test_num = [-1, -2, 0, -3, 4, 3, 2, 1, 0]
        self.test_num_ascending = sorted(self.test_num)
        self.test_num_descending = sorted(self.test_num, reverse=True)

    def test_pop_from_empty_heap(self):
        h = heap()
        with self.assertRaises(Exception):
            h.pop()

    def test_get_top_of_empty_heap(self):
        h = heap()
        with self.assertRaises(Exception):
            h.get_top()

    def test_correctness_of_min_heap(self):
        h = heap()
        for i in self.test_num:
            h.push(i)

        for i in range(len(self.test_num_ascending)):
            self.assertEqual(h.pop(), self.test_num_ascending[i])

    def test_correctness_of_max_heap(self):
        h = heap(is_min_heap=False)
        for i in self.test_num:
            h.push(i)

        for i in range(len(self.test_num_descending)):
            self.assertEqual(h.pop(), self.test_num_descending[i])
