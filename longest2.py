s = "pwwkew"

a_pointer = 0
b_pointer = 0
r_max = 0

in_list = []

while b_pointer < len(s):
    if s[b_pointer] not in in_list:
        in_list.append(s[b_pointer])
        r_max = max(len(in_list), r_max)
        b_pointer += 1
    else:
        in_list.remove(s[a_pointer])
        a_pointer += 1
print(r_max)


    