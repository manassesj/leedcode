class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head = ListNode( 1,  ListNode( 2,  ListNode( 2,  ListNode( 1,  None))))

head = ListNode( 1,  ListNode( 2, None))

self.current_node = head
self.flag = True

def reverse_list(node, current_node):
    if node is not None:
        reverse_list(node.next)
        if node.val == current_node.val:
            current_node = current_node.next
        else:
            self.flag = False
reverse_list(head)

return self.flag