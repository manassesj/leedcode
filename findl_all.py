nums = [4,3,2,7,8,2,3,1]

nums2 = set(nums)

nums_full = set([i + 1 for i in range(len(nums))])

b = nums_full - nums2
print(list(b))