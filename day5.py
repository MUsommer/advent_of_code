from helper_functions import get_data
import numpy as np

###### Data #######

data = get_data("day5.txt")

data = [x.rsplit(" -> ", 1) for x in data]
for i in range(0, len(data)):
    tmp_ = []
    for j in data[i]:
        tmp_var = [int(x) for x in j.rsplit(",")]
        tmp_.append(tuple(tmp_var))
    data[i] = tuple(tmp_)

# find array shape
def get_arr_shape(data):
    for i in range(0, len(data)):
        for j in data[i]:
            x = j[0]
            y = j[1]
            if i == 0:
                min_x = x
                min_y = y
                max_x = x
                max_y = y
            else:
                if x > max_x:
                    max_x = x
                if x < min_x:
                    min_x = x
                if y > max_y:
                    max_y = y
                if y < min_y:
                    min_y = y
    result = tuple([max_y - min_y + 1, max_x - min_x + 1]) # +1                
    print(f"Shape: {result}")
    print(f"X: {max_x} {min_x}",
        f"Y: {max_y} {min_y}", sep="\n")
    return result

###### Part One #######

def part_1(data):
    # creating an array to store counts
    arr_shape = get_arr_shape(data)
    arr = np.zeros(arr_shape)

    for i in range(0, len(data)):
        coordinates_dict = {}
        
        for j in range(0, len(data[i])): 
            coordinates_dict[f"x{j+1}"] = data[i][j][0] - 10 # -10 to align with array index
            coordinates_dict[f"y{j+1}"] = data[i][j][1] - 10 # -10 to align with array index
        
        x1 = coordinates_dict["x1"]
        x2 = coordinates_dict["x2"]
        y1 = coordinates_dict["y1"]
        y2 = coordinates_dict["y2"]
        
        if x1 == x2:
            x = x1
            y_vals = [y1, y2]
            min_y = min(y_vals)
            max_y = max(y_vals)
            
            # adding points on lines to array
            arr[x, min_y:max_y + 1] += 1
            
        elif y1 == y2:
            y = y1
            x_vals = [x1, x2]
            min_x = min(x_vals)
            max_x = max(x_vals)
            
            # adding points on lines to array
            arr[min_x:max_x + 1, y] += 1
        else:
            pass
    result = (arr >= 2).sum()
    return result
answer_1 = part_1(data)
print(f"Answer (part one): There are {answer_1} points where lines intersect.")

###### Part Two #######

def part_2(data):
    # creating an array to store counts
    arr_shape = get_arr_shape(data)
    arr = np.zeros(arr_shape)

    for i in range(0, len(data)):
        coordinates_dict = {}
        for j in range(0, len(data[i])):
            coordinates_dict[f"x{j+1}"] = data[i][j][0] - 10
            coordinates_dict[f"y{j+1}"] = data[i][j][1] - 10
        
        x1 = coordinates_dict["x1"]
        x2 = coordinates_dict["x2"]
        y1 = coordinates_dict["y1"]
        y2 = coordinates_dict["y2"]

        x_vals = [x1, x2]   
        y_vals = [y1, y2]
        min_x = min(x_vals)
        max_x = max(x_vals)
        min_y = min(y_vals)
        max_y = max(y_vals)
            
        if x1 == x2:
            x = x1
            arr[x, min_y:max_y + 1] += 1
        elif y1 == y2:
            y = y1
            arr[min_x:max_x + 1, y] += 1
        else:
            delta_x = max_x - min_x
            for m in range(0, delta_x + 1):
                if x1 < x2:
                    x = x1 + m
                else:
                    x = x1 - m
                if y1 < y2:
                    y = y1 + m
                else:
                    y = y1 - m
                arr[x, y] += 1
    result = (arr >= 2).sum()
    return result
answer_2 = part_2(data)
print(f"Answer (part one): There are {answer_2} points where lines intersect.")