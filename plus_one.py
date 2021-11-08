digits = [4,3,2,9]

number = ""

for n in digits:
    number += "{}".format(n)

number = int(number) + 1
number = str(number)

r = [int(n) for n in number]
print(r)

