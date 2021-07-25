from math import inf

input = [
    [1, 3, 15, 11, 2],
    [23, 127, 235, 19, 8]
]

def solution(input, menor, result):
    for i in input[0]:
        for j in input[1]:
            if i - j < menor and (i - j) >= 0:
                menor = (i - j)
                result[0],result[1] = i, j
    
    return result

result = [None] * 2
menor = inf

print(solution(input, menor, result))