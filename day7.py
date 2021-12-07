import numpy as np
from helper_functions import get_data

###### Data #######

data = get_data("day7.txt")
data = np.array([int(x) for x in data[0].rsplit(",")])

###### Part One #######

def part_1(data):
    min_ = data.min()
    max_ = data.max()
    sum_ = data.sum()

    for i in range(min_, max_+1):
        sums = 0
        for j in data:
            sums += abs(j - i)
        if i == 0:
            best_sum = sums
        elif sums < best_sum:
            best_sum = sums
    return best_sum
answer_1 = part_1(data)
print(f"Answer (part one): {answer_1}")

###### Part Two #######

def part_2(data):
    min_ = data.min()
    max_ = data.max()
    sum_ = data.sum()

    for i in range(min_, max_+1):
        sums = 0
        for j in data:
            delta = abs(j - i)
            sums += (delta * (delta + 1)) / 2
        if i == 0:
            best_sum = sums
        elif sums < best_sum:
            best_sum = sums
    return best_sum
answer_2 = part_2(data)
print(f"Answer (part two): {answer_2}")