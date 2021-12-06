from helper_functions import get_data

###### Data #######

def split_by_delimiter(data, delimiter=" "):
    dist_list = []
    command_list = []

    for i in data:
        split_loc = i.rfind(delimiter)
        
        distance = int(i[split_loc + 1:])
        dist_list.append(distance)
        
        command = i[:split_loc]
        command_list.append(command)
    print(f"Commands: {len(data)}",
          f"Distances: {len(dist_list)}", sep="\n")
    return dist_list, command_list

data = get_data("day2.txt")
dist_list, command_list = split_by_delimiter(data)

###### Part One #######

def get_coordinates(dist_list, command_list):
    x_pos = 0
    y_pos = 0

    for i in range(0, len(command_list)):
        command = command_list[i]
        dist = dist_list[i]
        
        if command == "forward":
            x_pos += dist
        elif command == "up":
            y_pos -= dist
        else:
            y_pos += dist
    print(f"X: {x_pos} Y: {y_pos}")
    return x_pos, y_pos

x_pos, y_pos = get_coordinates(dist_list, command_list)
answer_1 = x_pos * y_pos
print(f"Answer (part one): {answer_1}")

###### Part Two #######

def get_coordinates_with_aim(command_list, dist_list):  
    x_pos = 0
    y_pos = 0
    aim = 0

    for i in range(0, len(command_list)):
        command = command_list[i]
        dist = dist_list[i]

        if command == "forward":
            aim_x = aim * dist 
            x_pos += dist
            y_pos += aim_x
        elif command == "up":
            aim -= dist
        else:
            aim += dist
    print(f"X: {x_pos} Y: {y_pos}")
    return x_pos, y_pos

x_pos, y_pos = get_coordinates_with_aim(command_list, dist_list)
answer_2 = x_pos * y_pos
print(f"Answer (part two): {answer_2}")