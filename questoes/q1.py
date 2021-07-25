input2 = [1, 10, 2, 2, 10, 3, 3, 3, 4, 5, 5]
input = ["G", "e", "e", "k", "s"]

hash_size = len(input)
hash_list = [None] * hash_size

for i in input:
    if isinstance(i, str):
        hash_key = ord(i) % hash_size
    else:
        hash_key = i % hash_size

    if hash_list[hash_key] is None:
        hash_list[hash_key] = [i]
    else:
        if i not in hash_list[hash_key]:
            hash_list[hash_key].append(i)
    
result = "["

for j in hash_list:
    if j is not None:
        for x in j:
            result += "{} ".format(x)

print("{}]".format(result[:-1]))