from helper_functions import get_data

###### Data #######

def to_int(data):
    for i in range(0, len(data)):
        data[i] = int(data[i])
    return data

data = get_data("day1.txt")
data = to_int(data)

###### Part One #######

def part_1(data):
    counter = 0
    for i in range(0, len(data)):
        if data[i] > data[i-1]:
            counter += 1
    return counter

answer_1 = part_1(data)
print(f"Answer (part one): {answer_1}")

###### Part Two #######

def part_2(data):
    counter = 0
    len_ = len(data)
    for i in range(0, len_):
        window_start = i
        window_end = i + 3  
        if window_end < len_:
            current_window = sum(data[window_start:window_end])
            next_window = sum(data[window_start+1:window_end+1])

            if next_window > current_window:
                counter += 1
    return counter

answer_2 = part_2(data)
print(f"Answer (part two): {answer_2}")
