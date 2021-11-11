class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right






nums = [-10,-3,0,5,9,10]

num_size = len(nums)

print(nums[num_size//2])

if num_size % 2 == 1:
    print(nums[num_size//2])