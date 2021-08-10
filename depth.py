class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3, TreeNode(9, None, None), TreeNode(
    20, TreeNode(15, None, None), TreeNode(7, None, None)))


result = [0]


def depth(result, node, sum):
    if node != None:
        depth(result, node.left, sum + 1)
        depth(result, node.right, sum + 1)
    else:
        if result[0] < sum:
            result[0] = sum

depth(result, root, 0)

print(result[0])