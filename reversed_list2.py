class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
''

head = ListNode(1,  ListNode(2,  ListNode(
    3,  ListNode(4,  ListNode(5,  None)))))


prev = None
curr = head

while curr is not None:
    nextNode = curr.next 
    curr.next = prev
    prev = curr
    curr = nextNode