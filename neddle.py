haystack = "heoxx"
needle = "ll"

h_len = len(haystack)
n_len = len(needle)

if n_len == 0:
    print(0)

a_index = 0
b_index = len(needle)
flag = False

while b_index <= h_len:
    print(a_index, b_index)
    print(haystack[a_index:b_index])
    if haystack[a_index:b_index] != needle:
        a_index += 1
        b_index += 1
    else:
        flag = True
        break

if flag == True:
    print(a_index)
else:
    print(-1)