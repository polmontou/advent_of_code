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

