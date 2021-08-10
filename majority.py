nums =  [2,2,1,1,1,2,2]
hash_size = len(nums)
hash_table = [None] * hash_size

for n in nums:
    hash_key = abs(n) % hash_size

    if hash_table[hash_key] is None:
        hash_table[hash_key] = [[n, 1]]
    else:
        flag = False

        for e in hash_table[hash_key]:
            if e[0] == n:
                e[1] += 1
                flag = True

        if flag is False:
            hash_table[hash_key].append([n, 1])
for x in hash_table:
    if x is not None:
        for y in x:
            if y[1] > (hash_size / 2):
                return y[0]
                break