
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode( 1,  TreeNode( 2,  TreeNode( 2,  None,  None),  None),  TreeNode( 2,  TreeNode( 2,  None,  None),  None))


def func(nodo):

    func(nodo.left) 
    func(nodo.right) 