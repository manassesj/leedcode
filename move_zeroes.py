nums = [0,1,0,3,12]
t = nums.count(0)

zeros = [0] * t

for x in range(t):
    nums.remove(0)
nums.extend(zeros)
