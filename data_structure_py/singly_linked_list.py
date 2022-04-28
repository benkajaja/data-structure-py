"""Implementation of singly linked list.

  Typical usage example:
    sll = SinglyLinkedList()
    sll.append()
    sll.prepend()
    val = sll.pop(1)
    for node in sll: print(node.val)
"""


class SinglyLinkedNode:
    """SinglyLinkedNode class

    Attributes:
        val: The value of this node
        next_node: The object of next node
    """

    def __init__(self, val: int = 0, next_node=None) -> None:
        self.next_node = next_node
        self.val = val


class SinglyLinkedList:
    """SinglyLinkedList class

    Methods:
        append()
        prepend()
        pop()

    Iterator
    """

    def __init__(self) -> None:
        self.length = 0
        self.head = SinglyLinkedNode()
        self.tail = self.head
        self.__iter_idx = self.head

    def append(self, val: int) -> None:
        """Append an item to the tail"""
        self.tail.next_node = SinglyLinkedNode(val)
        self.tail = self.tail.next_node
        self.length += 1

    def prepend(self, val: int) -> None:
        """Prepend an item to the head"""
        remain_list = self.head.next_node
        self.head.next_node = SinglyLinkedNode(val, remain_list)
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

        pre, cur = SinglyLinkedNode(0, self.head), self.head
        while index:
            pre = pre.next_node
            cur = cur.next_node
            index -= 1

        pre.next_node = cur.next_node

        if cur == self.tail:
            self.tail = pre

        self.length -= 1

        return cur.val

    def __iter__(self):
        self.__iter_idx = self.head
        return self

    def __next__(self) -> SinglyLinkedNode:
        self.__iter_idx = self.__iter_idx.next_node

        if self.__iter_idx is None:
            raise StopIteration

        return self.__iter_idx
