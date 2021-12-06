from helper_functions import get_data
import numpy as np

###### Data #######

data = get_data("day4.txt")

# get numbers from first item and split string by comma -> add to list
nums = data[0].rsplit(",")
nums = [int(x) for x in nums]

# get 5x5 boards from itm 2 +
rows = [[x for x in [int(x) for x in x.rsplit(" ") if x != ""]] for x in data[2:] if x != ""]
boards = []
for i in range(0, len(rows), 5):
    boards.append(rows[i:i+5])
boards = np.array(boards)

###### Part One #######

def part_1(nums, boards):
    count_dict = {}
    
    for j in range(0, len(nums)):
        num = nums[j]
        # board for board
        for i in range(0, len(boards)):
            # checking rows in board
            for x in range(0, 5):
                if num in boards[i][x,:]:
                    key_name = f"board_{i}_row{x}"
                    if key_name in count_dict.keys():
                        count_dict[key_name] += 1
                        if count_dict[key_name] == 5:
                            sum_marked = sum([x for x in boards[i].ravel() if x in nums[:j + 1]])
                            sum_unmarked = boards[i].sum() - sum_marked
                            return sum_unmarked * num         
                    else:
                        count_dict[key_name] = 1
            # checking cols in board
            for x in range(0, 5):
                if num in boards[i][:, x]:
                    key_name = f"board_{i}_col{x}"
                    if key_name in count_dict.keys():
                        count_dict[key_name] += 1
                        if count_dict[key_name] == 5:
                            sum_marked = sum([x for x in boards[i].ravel() if x in nums[:j + 1]])
                            sum_unmarked = boards[i].sum() - sum_marked
                            return sum_unmarked * num          
                    else:
                        count_dict[key_name] = 1

answer_1 = part_1(nums, boards)
print(f"Answer (part one): {answer_1}")

###### Part Two #######

def part_2(nums, boards):
    count_dict = {}
    finished_boards = []
    n_boards = len(boards)
    
    for j in range(0, len(nums)):
        num = nums[j]
        for i in range(0, len(boards)):
            #print(len(finished_boards))
            if i not in finished_boards:
                for x in range(0, 5):
                    if num in boards[i][x,:]:
                        key_name = f"board_{i}_row{x}"
                        if key_name in count_dict.keys():
                            count_dict[key_name] += 1
                            if count_dict[key_name] == 5:
                                finished_boards.append(i)
                                remaining_boards = n_boards - len(finished_boards)
                                if remaining_boards == 0:
                                    sum_marked = sum([x for x in boards[i].ravel() if x in nums[:j + 1]])
                                    sum_unmarked = boards[i].sum() - sum_marked
                                    print(sum_marked, sum_unmarked, j)
                                    return sum_unmarked * num   
                        else:
                            count_dict[key_name] = 1
            if i not in finished_boards:
                for x in range(0, 5):
                    if num in boards[i][:, x]:
                        key_name = f"board_{i}_col{x}"
                        if key_name in count_dict.keys():
                            count_dict[key_name] += 1
                            if count_dict[key_name] == 5:
                                finished_boards.append(i)
                                remaining_boards = n_boards - len(finished_boards)
                                if remaining_boards == 0:
                                    sum_marked = sum([x for x in boards[i].ravel() if x in nums[:j + 1]])
                                    sum_unmarked = boards[i].sum() - sum_marked
                                    print(sum_marked, sum_unmarked, j)
                                    return sum_unmarked * num   
                        else:
                            count_dict[key_name] = 1
answer_2 = part_2(nums, boards)
print(f"Answer (part two): {answer_2}")