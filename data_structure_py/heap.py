"""Implementation of heap.

  Typical usage example:
    myHeap = Heap()
    myHeap.push(1)
    val = myHeap.get_top()
    val = myHeap.pop()
"""


class Heap:
    """Heap class

    Attributes:
        is_min_heap: A boolean indicating if we use minHeap or maxHeap.

    Methods:
        push()
        pop()
        get_top()
    """

    def __init__(self, is_min_heap: bool = True):
        self.heap = []
        self.__inverse = is_min_heap

    def __comp(self, first: int, second: int) -> bool:
        return (first < second) ^ self.__inverse

    def __upheap(self) -> None:
        cur_pos = len(self.heap)-1
        last_val = self.heap[cur_pos]
        while cur_pos > 0:
            parent_pos = (cur_pos - 1) // 2
            if self.__comp(self.heap[parent_pos], last_val):
                self.heap[cur_pos] = self.heap[parent_pos]
                cur_pos = parent_pos
            else:
                break
        self.heap[cur_pos] = last_val

    def __downheap(self) -> None:
        cur_pos = 0
        first_val = self.heap[cur_pos]

        while cur_pos*2 + 1 < len(self.heap):
            left_pos = cur_pos*2 + 1
            right_pos = cur_pos*2 + 2

            left_val = self.heap[left_pos]
            right_val = self.heap[right_pos] if right_pos < len(
                self.heap) else None

            if right_val is not None:
                if (not self.__comp(first_val, left_val) and not self.__comp(first_val, right_val)):
                    break

                if self.__comp(left_val, right_val):
                    self.heap[cur_pos] = right_val
                    cur_pos = right_pos
                else:
                    self.heap[cur_pos] = left_val
                    cur_pos = left_pos
            else:
                if not self.__comp(first_val, left_val):
                    break

                self.heap[cur_pos] = left_val
                cur_pos = left_pos

        self.heap[cur_pos] = first_val

    def push(self, item: int) -> None:
        """Push an item into heap"""
        self.heap.append(item)
        self.__upheap()

    def pop(self) -> int:
        """Pop an item from the top"""
        if len(self.heap) == 0:
            raise Exception("Cannot pop from an empty heap!")

        val = self.heap.pop(0)

        if len(self.heap) != 0:
            self.heap.insert(0, self.heap.pop())
            self.__downheap()

        return val

    def get_top(self) -> int:
        """Get the top item of the heap"""
        if len(self.heap) == 0:
            raise Exception("Cannot get top item from an empty heap!")

        return self.heap[0]
