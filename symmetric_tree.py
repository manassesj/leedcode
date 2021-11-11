class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#root = TreeNode( 1,  TreeNode( 2,  TreeNode( 2,  None,  None),  None),  TreeNode( 2,  TreeNode( 2,  None,  None),  None))

#root = TreeNode( 1,  TreeNode( 2,  TreeNode( 3,  None,  None),  TreeNode( 4,  None,  None)),  TreeNode( 2,  TreeNode( 4,  None,  None),  TreeNode( 3,  None,  None)))
root = TreeNode( 1,  
TreeNode( 2, None,  TreeNode( 3,  None,  None)),  
TreeNode( 2,  None,  TreeNode( 3,  None,  None))
)

class Solution():
    
    def __init__(self):
        self.in_or1 = ""
    def in_order(self, node):
        if node is not None:
            if node.left == None and node.right != None:
                self.in_or1 += "S"
                self.in_or1 += str(node.val)
                self.in_order(node.right)
            elif node.left != None and node.right == None:
                self.in_order(node.left)
                self.in_or1 += str(node.val)
                self.in_or1 += "S"
            elif node.left != None and node.right != None:
                self.in_order(node.left)
                self.in_or1 += str(node.val)
                self.in_order(node.right)
            elif node.left == None and node.right == None:
                self.in_or1 += str(node.val)
c = Solution()
c.in_order(root)
left = c.in_or1
print(left) 
