class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode( 3,  TreeNode( 9,  None,  None), 
TreeNode( 20,  TreeNode( 15,  None,  None), 
TreeNode( 7,  None,  None)))

class Solution():

    def __init__(self):
        self.depth = 0
    
    def func(self, nodo, current_depth):
        if nodo is not None:
            self.depth = max(current_depth + 1, self.depth)
            self.func(nodo.left, current_depth + 1)
            self.func(nodo.right, current_depth + 1)


c = Solution()
c.func(root, 0)
print(c.depth)