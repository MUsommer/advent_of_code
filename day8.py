from helper_functions import get_data

###### Data #######

data = get_data("day8.txt")
data = [x.rsplit(" | ") for x in data]
data = [x.rsplit(" ") for y in data for x in y]
print("len: ", len(data))

###### Part One #######

def part_1(data, digits, digit_lens):
    digit_dict = dict(zip(digit_lens, digits))
    digit_count = dict(zip(digits, [0] * len(digits)))

    for i in range(0, len(data), 2):
        lens_to_find = [len(x) for x in data[i + 1] if len(x) in digit_lens]
        for j in lens_to_find:
            digit_count[digit_dict[j]] += 1

    return digit_count

digits = [1,4,7,8]
digit_lens = [2, 4, 3, 7]

result = part_1(data, digits, digit_lens)
answer_1 = sum(result.values())
print(f"Answer (part one): {answer_1}")