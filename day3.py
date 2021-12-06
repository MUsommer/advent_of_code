from helper_functions import get_data

###### Data #######

data = get_data("day3.txt")

###### Part One #######

def get_gamma_epsilon(data):
    itm_len = len(data[0])
    lst_len = len(data)
    lst_len_mid = int(lst_len / 2)
    
    gamma = ""
    epsilon = ""

    for i in range(0, itm_len):
        count_1 = sum([int(x[i]) for x in data])
        
        if count_1 > lst_len_mid:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon

def binary_converter(digit):
    len_ = len(digit)
    counter = len_ - 1
    decimal = 0
    
    for i in range(0, len_):
        bit_val = int(digit[i]) * (2 ** counter)
        decimal += bit_val
        counter -= 1
    return decimal

gamma, epsilon = get_gamma_epsilon(data)
gamma = binary_converter(gamma)
epsilon = binary_converter(epsilon)
answer_1 = gamma * epsilon
print(f"Answer (part 1): {answer_1}")

###### Part Two #######

def oxygen_rating(data):
    itm_len = len(data[0])
    
    for i in range(0, itm_len):
        count_1 = sum([int(x[i]) for x in data])
        count_0 = len(data) - count_1

        if count_1 >= count_0:
            to_keep = "1"
        else:
            to_keep = "0"
            
        data = [x for x in data if x[i] == to_keep]
        
        if len(data) == 1:
            break
    return data[0]

def co2_rating(data):
    itm_len = len(data[0])
    tmp_data = data
    
    for i in range(0, itm_len):
        count_0 = len([x for x in tmp_data if x[i] == "0"])
        count_1 = len(tmp_data) - count_0
        
        if count_1 >= count_0:
            to_keep = "0"
        else:
            to_keep = "1"
        tmp_data = [x for x in tmp_data if x[i] == to_keep]
        if len(tmp_data) == 1:
            break
    return tmp_data[0]

oxygen = oxygen_rating(data)
oxygen = binary_converter(oxygen)

co2 = co2_rating(data)
co2 = binary_converter(co2)

answer_2 = oxygen * co2
print(f"Answer (part 2): {answer_2}")