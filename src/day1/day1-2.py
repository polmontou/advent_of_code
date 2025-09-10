import re

file_path = "set.txt"

written_base = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
corresponding_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

with open(file_path, 'r') as f:
    content = f.readlines()
    x = []
    for line in content:
        y = []
        for i, letter in enumerate(line):
            for j, written_number in enumerate(written_base):
                corresponding = True
                for k, letter_number in enumerate(written_number):
                    if corresponding:
                        if (i + k)<len(line) and line[i+k] != written_base[j][k]:
                            corresponding = False
                if corresponding:
                    y.append(corresponding_base[j])
        x.append(y)

answer = 0

for line in x:
    first = 0
    last = 0
    for number in line:
        if first == 0 and 0 < number <= 9:
            first = number
        if first != 0 and 0 < number <= 9:
            last = number
    number = first*10 + last
    answer += number
print(answer)

# def convert_str_to_int(string):
#     match string:
#         case"zero":
#             return 0
#         case "one":
#             return 1
#         case "two":
#             return 2
#         case "three":
#             return 3
#         case "four":
#             return 4
#         case "five":
#             return 5
#         case "six":
#             return 6
#         case "seven":
#             return 7
#         case "eight":
#             return 8
#         case "nine":
#             return 9
#
# with open(file_path, 'r') as f:
#     content = f.readlines()
#     answer = 0
#     pattern = r"(?=(\d{1}|one|two|three|four|five|six|seven|eight|nine))"
#     for line in content:
#         number_found = re.findall(pattern, line)
#
#         if number_found[0].isdigit():
#             first = int(number_found[0])
#         else:
#             first = convert_str_to_int(number_found[0])
#
#         if number_found[-1].isdigit():
#             last = int(number_found[-1])
#         else:
#             last = convert_str_to_int(number_found[-1])
#
#         number = first*10+last
#         answer += number
#
#     print(answer)


