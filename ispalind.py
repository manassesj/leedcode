s = "A man, a plan, a canal: Panama"

result = ""

for c in s:
    if c.isalpha() or c.isnumeric():
        result += "{}".format(c.lower())

if result == result[::-1]:
    print(True)
else:
    print(False)
