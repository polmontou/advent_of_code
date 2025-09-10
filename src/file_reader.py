file_path = "../keys.txt"

with open(file_path, 'r') as f:
    content = f.readlines()
    answer = 0
    for i, line in enumerate(content):
        number = 0
        reversed_line = line[::-1]
        for char in line:
            if char.isdigit():
                number = int(char)*10
                break
        for char in reversed_line:
            if char.isdigit():
                number += int(char)
                break
        answer += number
    print(answer)