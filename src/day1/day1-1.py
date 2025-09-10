file_path = "set.txt"

with open(file_path, 'r') as f:
    content = f.readlines()
    answer = 0
    for line in content:
        first = 0
        last = 0
        for char in line:
            if char.isdigit():
                if first == 0 and 0 < int(char) <= 9:
                    first = char
                if first != 0 and 0 < int(char) <= 9:
                    last = char
        number = first + last
        answer += int(number)
    print(answer)