nums = [-2,1,-3,4,-1,2,1,-5,4]

def get_max(nums):
    index = 0
    while index < len(nums) - 1:
        if nums[index] > 0:
            nums[index + 1] += nums[index]
        
        index += 1
    
    return nums

t = get_max(nums)
print(t)