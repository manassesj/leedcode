class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode( 1,  ListNode( 2,  ListNode( 2,  ListNode( 1,  None))))

result = ""

current_node = head

while current_node is not None:
    result += str(current_node.val)
    current_node = current_node.next

print(result)

s = 0
e = len(result) - 1

flag = True

while s < e:
    print(s, e)
    if result[s] == result[e]:
        s += 1 
        e -= 1
    else:
        flag = False
        break

print(flag)



