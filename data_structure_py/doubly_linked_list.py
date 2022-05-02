"""Implementation of doubly linked list.

  Typical usage example:
    dll = DoublyLinkedList()
    dll.append()
    dll.prepend()
    val = dll.pop(1)
    for node in dll: print(node.val)
"""


class DoublyLinkedNode:
    """DoublyLinkedNode class

    Attributes:
        val: The value of this node
        pre_node: The object of previous node
        next_node: The object of next node
    """

    def __init__(self, val: int = 0, pre_node=None, next_node=None) -> None:
        self.pre_node = pre_node
        self.next_node = next_node
        self.val = val


class DoublyLinkedList:
    """DoublyLinkedList class

    Methods:
        append()
        prepend()
        pop()

    Iterator
    """

    def __init__(self) -> None:
        self.length = 0
        self.head = DoublyLinkedNode()
        self.tail = self.head
        self.__iter_idx = self.head

    def append(self, val: int) -> None:
        """Append an item to the tail"""
        self.tail.next_node = DoublyLinkedNode(val, pre_node=self.tail)
        self.tail = self.tail.next_node
        self.length += 1

    def prepend(self, val: int) -> None:
        """Prepend an item to the head"""
        remain_list = self.head.next_node
        self.head.next_node = DoublyLinkedNode(
            val, pre_node=self.head, next_node=remain_list)

        if remain_list:
            remain_list.pre_node = self.head.next_node

        if self.tail == self.head:
            self.tail = self.head.next_node
        self.length += 1

    def pop(self, index: int = None) -> int:
        """Pop an item with specific index (1-index). Default index points to the tail."""
        if not index:
            index = self.length
        if self.length == 0:
            raise Exception("Cannot pop from an empty linked list")
        if index < 1:
            raise Exception("Index could not less than 1")
        if index > self.length:
            raise Exception("Pop index is outside the linked list")

        cur = self.head
        while index:
            cur = cur.next_node
            index -= 1

        cur.pre_node.next_node = cur.next_node

        if cur.next_node:
            cur.next_node.pre_node = cur.pre_node

        if cur == self.tail:
            self.tail = cur.pre_node

        self.length -= 1
        return cur.val

    def __iter__(self):
        self.__iter_idx = self.head
        return self

    def __next__(self) -> DoublyLinkedNode:
        self.__iter_idx = self.__iter_idx.next_node

        if self.__iter_idx is None:
            raise StopIteration

        return self.__iter_idx
