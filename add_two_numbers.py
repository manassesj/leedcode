class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode( 2,  ListNode( 4,  ListNode( 3,  None)))
l2 = ListNode( 5,  ListNode( 6,  ListNode( 4,  None)))

class solution():

    def __init__(self) -> None:
        self.first = ""
        self.second = ""



    # def get_nums(self,l1, l2):
    #     if l1 is not None:
    #         self.get_nums(l1.next, l2)
    #         self.first += str(l1.val)
    #     if l2 is not None:
    #         self.get_nums(l1, l2.next)
    #         self.second += str(l2.val)


    def get_nums(self,root, flag):
        if root is not None:
            self.get_nums(root.next, flag)
            if flag:
                self.first += str(root.val)
            else:
                self.second += str(root.val)

    def build_list(self, number):
        root = None
        last = None
        i = len(number) - 1
        while i >= 0:
            node = ListNode(val=number[i])
            if root is None:
                root = last = node
            else:
                last.next = node
                last = node
            i -= 1

        return root

c = solution()
c.get_nums(l1, True)
c.get_nums(l2, False)
c.build_list(str(int(c.first) + int(c.second)))

print(c.first)
print(c.second)



