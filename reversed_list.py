class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
''

head = ListNode(1,  ListNode(2,  ListNode(
    3,  ListNode(4,  ListNode(5,  None)))))

new_head = [None]
new_tail = [None]

def solution(new_head, new_tail, current_node):
    if current_node is not None:
        solution(new_head, new_tail, current_node.next)
        new_node = ListNode(val=current_node.val)
        if new_head[0] is None:
            new_head[0] = new_tail[0] = new_node
        else:
            new_tail[0].next = new_node
            new_tail[0] = new_node


solution(new_head, new_tail, head)

print(new_head)
