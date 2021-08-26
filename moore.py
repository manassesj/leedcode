n_list = [1, 2, 5, 3, 2]

me = n_list[0]
count = 1

for n in n_list:
    if  n == me:
        count += 1
    else:
        count -= 1

    if count == 0:
        me = n
        count = 1

if n_list.count(me) > len(n_list) // 2:
    print(me)
else:
    print("No majority element")