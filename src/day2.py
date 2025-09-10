import re

file_path = "../keys.txt"

def convert_str_to_int(string):
    match string:
        case"zero":
            return 0
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9

with open(file_path, 'r') as f:
    content = f.readlines()
    answer = 0
    pattern = r"(?=(\d{1}|one|two|three|four|five|six|seven|eight|nine))"
    for line in content:
        number_found = re.findall(pattern, line)
        if number_found[0].isdigit():
            first = int(number_found[0])
        else:
            first = convert_str_to_int(number_found[0])
        if number_found[-1].isdigit():
            last = int(number_found[-1])
        else:
            last = convert_str_to_int(number_found[-1])
        number = first*10+last
        answer += number
    print(answer)


