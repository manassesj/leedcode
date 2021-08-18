class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root1 = TreeNode( 1,  TreeNode( 3,  TreeNode( 5,  None,  None),  None),  TreeNode( 2,  None,  None))
root2 = TreeNode( 2,  TreeNode( 1,  None,  TreeNode( 4,  None,  None)),  TreeNode( 3,  None,  TreeNode( 7,  None,  None)))

def recursion(self, root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    root1.val += root2.val
    root1.left = recursion(root1.left, root2.left)



    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root1 = TreeNode( 1,  TreeNode( 3,  TreeNode( 5,  None,  None),  None),  TreeNode( 2,  None,  None))
root2 = TreeNode( 2,  TreeNode( 1,  None,  TreeNode( 4,  None,  None)),  TreeNode( 3,  None,  TreeNode( 7,  None,  None)))

def recursion(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    root1.val += root2.val
    root1.left = recursion(root1.left, root2.left)
    root1.right = recursion(root1.right, root2.right)
    return root1

return recursion(root1, root2)




    