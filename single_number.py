nums = [4,1,2,1,2]

hash_size = len(nums)
hash_table = [None] * hash_size

for n in nums: 
    hash_key = n % hash_size

    if hash_table[hash_key] is not None:
        if n in hash_table[hash_key]:
            hash_table[hash_key].remove(n)
        else:
            hash_table[hash_key].append(n)
    else:
        hash_table[hash_key] = [n]

print(hash_table)

for e in hash_table:
    if e is not None and len(e) > 0:
        print(e[0])
        break
