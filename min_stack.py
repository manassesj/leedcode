class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None

class MinStack:
    def __init__(self):
        self.tail = None

    def push(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail = new_node
    def pop(self) -> None:
        self.tail = self.tail.prev

    def top(self) -> int:
        return self.tail.val

    def getMin(self) -> int:
        min = self.tail.val
        curr_node = self.tail
        while curr_node is not None:
            if curr_node.val < min:
                min = curr_node.val
            curr_node = curr_node.prev
        
        return min
