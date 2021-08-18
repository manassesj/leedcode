n = int(input())

result = []

while n != 0:
    if n % 2 != 0:
        n -= 1
    else:
        result.append(n)
        n -= 2

i = len(result) - 1

while i >= 0:
    print(result[i])
    i -=1