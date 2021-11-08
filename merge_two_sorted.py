nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

for n in nums2:
    for i, n2 in enumerate(nums1):
        if n > n2:
            nums1.insert(i-1, n)

print(nums1)