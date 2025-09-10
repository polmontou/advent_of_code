import re

file_path = "set.txt"
game_set = {"blue":14,"green":13,"red":12}

with open(file_path, 'r') as f:
    content = f.readlines()
    id_pattern = r"Game (\d+):"
    blue_pattern = r"(\d+) blue"
    green_pattern = r"(\d+) green"
    red_pattern = r"(\d+) red"
    id_total = 0

    for line in content:
        blue_found = 0
        green_found = 0
        red_found = 0

        id = int(re.search(id_pattern, line).group(1))

        blue = re.findall(blue_pattern, line)
        for number in blue:
            if int(number) > blue_found:
                blue_found = int(number)

        green = re.findall(green_pattern, line)
        for number in green:
            if int(number) > green_found:
                green_found = int(number)

        red = re.findall(red_pattern, line)
        for number in red:
            if int(number) > red_found:
                red_found = int(number)

        print("parsed id => ", id, " blue : ", blue_found, " green : ", green_found, " red : ", red_found)
        if blue_found <= game_set["blue"] and green_found <= game_set["green"] and red_found <= game_set["red"]:
            print("valid id :", id)
            print(id_total, "+", id, "=", id_total+id)
            id_total += int(id)


    print(id_total)