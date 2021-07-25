s = "aabcccccaaa"

def compreesing(s):
    result = ""
    while True:
        idx_f = -1
        sum = -1
        c = ""
        prev_c = ""
        for i, char  in enumerate(s):
            prev_c = c
            c = char
            if idx_f == -1:
                idx_f = i
                sum = 1
                continue
            if prev_c == c:
                sum += 1
            else:
                result += "{}{}".format(prev_c, sum)
                c = char
                sum = 1
        result += "{}{}".format(prev_c, sum)
        print(result)
        break

compreesing(s)

