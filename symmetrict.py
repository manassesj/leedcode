
# Definition for a binary tree node.
result = []
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode( 1,  TreeNode( 2,  TreeNode( 3,  None,  None),  TreeNode( 4,  None,  None)),  TreeNode( 2,  TreeNode( 4,  None,  None),  TreeNode( 3,  None,  None)))

def inorderLeft(result, leftnode):
    if leftnode != None:
        inorderLeft(result, leftnode.left)
        result.append(leftnode.val)
        inorderLeft(result, leftnode.right)

def inorderRight(result, rightnode):
    if rightnode != None:
        inorderRight(result, rightnode.left)
        result.append(rightnode.val)
        inorderRight(result, rightnode.right)

inorderLeft(result, root.left)
result.append(root.val)
inorderRight(result, root.right)

s = 0
e = len(result) - 1

while s != e:
    if result[s] == result[e]:
        s += 1
        e -= 1
    else:
        print(False)
print(True)

print(result)


