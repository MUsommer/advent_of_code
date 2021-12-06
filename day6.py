from helper_functions import get_data

###### Data #######

data =  get_data("day6.txt")

data = [x.rsplit(",") for x in data][0]
data = [int(x) for x in data]

###### Part One #######

def fish_thing(fish_age):
    if fish_age == 0:
        fish_age = 6
        new_fish = True
    else:
        fish_age -= 1
        new_fish = False
    return fish_age, new_fish

def fish_count(data, days):
    fishes = data.copy()
    for i in range(0, days):
        for j in range(0, len(fishes)):
            fish_age, new_fish = fish_thing(fishes[j])
            fishes[j] = fish_age
            if new_fish:
                fishes.append(8)
    return len(fishes)
answer_1 = fish_count(data, days=80)
print(f"Answer (part one): {answer_1}")

###### Part Two #######

def part_2(data, days):
    fishes = data.copy()

    fish_dict = {}
    fish_keys = [0,1,2,3,4,5,6,7,8]

    for i in fish_keys:
        fish_dict[i] = 0
        
    for i in fishes:
        fish_dict[i] += 1
        
    age_flows = [6, 0, 1, 2, 3, 4, 5, 6, 7]
        
    for i in range(0, days):
        tmp_fish_dict = {}
        for i in fish_keys:
            tmp_fish_dict[i] = 0
            
        for key, value in fish_dict.items():
            if key == 0:
                tmp_fish_dict[8] += value
            tmp_fish_dict[age_flows[key]] += value
                
        for key, value in fish_dict.items():
            fish_dict[key] = tmp_fish_dict[key]
    return sum(fish_dict.values())
answer_2 = part_2(data, days=256)
print(f"Answer (part two): {answer_2}")