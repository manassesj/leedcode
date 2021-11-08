nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1,1,2]

nums = []

if len(nums) == 0:
    print(0)

a_pointer = 0
b_pointer = 1

while b_pointer < len(nums):
    if nums[a_pointer] != nums[b_pointer]:
        a_pointer += 1
        nums[a_pointer] = nums[b_pointer]
    b_pointer += 1

print(a_pointer + 1) 
