n = int(input())

persons = map(int, input().split())

lowerst = 21
index = 21

for i, p in enumerate(persons):
    if int(p) < lowerst:
        lowerst = int(p)
        index = i + 1

print(index)
