import re

file_path = "set.txt"
game_set = {"blue":14,"green":13,"red":12}

with open(file_path, 'r') as f:
    content = f.readlines()
    id_pattern = r"Game (\d+):"
    blue_pattern = r"(\d+) blue"
    green_pattern = r"(\d+) green"
    red_pattern = r"(\d+) red"
    total_power = 0

    for line in content:
        blue_found = 0
        green_found = 0
        red_found = 0

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

        print(green_found*red_found*blue_found)

        total_power += green_found * red_found * blue_found


    print(total_power)