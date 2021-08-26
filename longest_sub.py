s = "pwwkew"

hash_table = [None] * len(s)
hash_size = len(s)

a_pointer = 0
b_pointer = 0
max = 0

def len_hash_table(hash_table):
    count = 0
    for r in hash_table:
        if r is not None:
            count += len(r)
    return count

while b_pointer < hash_size:
    hash_key = ord(s[b_pointer]) % hash_size
    if hash_table[hash_key] is None or s[b_pointer] not in hash_table[hash_key]:
        if hash_table[hash_key] is None:
            hash_table[hash_key] = list(s[b_pointer])
        else:
            hash_table[hash_key].append(s[b_pointer])
        b_pointer += 1
        max_result = len_hash_table(hash_table)
        max = max_result if max_result > max else max
    else:
        hash_table[ord(s[a_pointer]) % hash_size].remove(s[a_pointer])
        a_pointer += 1

print(max)

