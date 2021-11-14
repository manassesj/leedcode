from math import inf

prices = [7,6,4,3,1]

lowest = inf
lowest_index = 0
index = 0

while index < len(prices) - 1:
    if  prices[index] < lowest:
        lowest = prices[index]
        lowest_index = index
    index += 1

if lowest_index == len(prices) - 1:
    print(0)
else:
    highest = lowest
    while lowest_index < len(prices):
        if prices[lowest_index] > highest:
            highest = prices[lowest_index]
        lowest_index += 1

    print(highest - lowest)
