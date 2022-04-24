class heap:

    def __init__(self, is_min_heap: bool = True):
        self.h = []
        self.__inverse = is_min_heap

    def __comp(self, a: int, b: int) -> bool:
        return (a < b) ^ self.__inverse

    def __upheap(self) -> None:
        cur_pos = len(self.h)-1
        last_val = self.h[cur_pos]
        while(cur_pos > 0):
            parent_pos = (cur_pos - 1) // 2
            if (self.__comp(self.h[parent_pos], last_val)):
                self.h[cur_pos] = self.h[parent_pos]
                cur_pos = parent_pos
            else:
                break
        self.h[cur_pos] = last_val

    def __downheap(self) -> None:
        cur_pos = 0
        first_val = self.h[cur_pos]

        while(cur_pos*2 + 1 < len(self.h)):
            left_pos = cur_pos*2 + 1
            right_pos = cur_pos*2 + 2

            left_val = self.h[left_pos]
            right_val = self.h[right_pos] if right_pos < len(self.h) else None

            if (right_val != None):
                if (not self.__comp(first_val, left_val) and not self.__comp(first_val, right_val)):
                    break
                elif (self.__comp(left_val, right_val)):
                    self.h[cur_pos] = right_val
                    cur_pos = right_pos
                else:
                    self.h[cur_pos] = left_val
                    cur_pos = left_pos
            else:
                if (not self.__comp(first_val, left_val)):
                    break
                else:
                    self.h[cur_pos] = left_val
                    cur_pos = left_pos

        self.h[cur_pos] = first_val

    def push(self, item: int) -> None:
        self.h.append(item)
        self.__upheap()

    def pop(self) -> int:
        if (len(self.h) == 0):
            raise Exception("Cannot pop from an empty heap!")

        val = self.h.pop(0)

        if (len(self.h) != 0):
            self.h.insert(0, self.h.pop())
            self.__downheap()

        return val

    def get_top(self) -> int:
        if (len(self.h) == 0):
            raise Exception("Cannot get top item from an empty heap!")

        return self.h[0]
