from samba import fault_setup

file_path = "set.txt"
digits = [0,1,2,3,4,5,6,7,8,9]
spec_chars =
# def find_int_in_line(text: str, line: int):
#     integers = []
#     indexes = []
#     founded_int_once = False
#     found_int = ""
#     lines = []
#     index = 0
#     found_int_ended = False
#
#     for i in range(len(text)):
#         if found_int_ended:
#             found_int_ended = False
#             founded_int_once = False
#         is_digit = False
#
#         for j, digit in enumerate(digits):
#             if  str(digit) == text[i]:
#                 found_int += text[i]
#                 if index == 0:
#                     index = i
#                 is_digit = True
#                 founded_int_once = True
#                 break
#
#         if founded_int_once:
#             if not is_digit:
#                 found_int_ended = True
#                 integers = integers + [found_int]
#                 found_int = ""
#                 indexes = indexes + [index]
#                 lines = lines + [line]
#                 index = 0
#
#     return integers, indexes, lines

def find_spec_chars(content: str):
    spec_chars = []
    not_spec_chars = digits + ["."]
    for line in content:
        for char in line:
            is_spec = True
            for not_spec_char in not_spec_chars:
                if char == str(not_spec_char):
                    is_spec = False
                    break

            if is_spec:
                is_registered = False
                for spec_char in spec_chars:
                    if char == spec_char:
                        is_registered = True
                if not is_registered:
                    spec_chars = spec_chars + [char]
    return spec_chars

def is_hint(char: str)-> bool:
    for digit in digits:
        if str(digit) == char:
            return True
    return False

def is_part(number: str, index: int, line: int, content):
    specs_chars = find_spec_chars(content)
    for digit in number:
        print(digit)

def parse_line(line: str, first_index: int, len: int, spec_chars) -> bool:
    for i in range(first_index-1, first_index+len+1):
        for spec_char in spec_chars:
            if line[i] == spec_char:
                return True
    return False



with open(file_path, 'r') as f:
    content = f.read()
    content_in_lines = f.readlines()
    spec_chars = find_spec_chars(content)
    started_int = False
    found_int = ""
    first_index = 0
    total = 0

    for i, line in enumerate(content_in_lines):
        for j, char in enumerate(line):
            if is_hint(char):
                started_int = True
                if first_index == 0:
                    first_index  = j
                found_int+= char
            else:
                if started_int:
                    is_part = False
                    int_length = len(found_int)
                    if i-1 >= 0 :
                        is_part = parse_line(content[i-1], first_index, int_length, spec_chars)
                    is_part = parse_line(line, first_index, int_length, spec_chars)
                    if i+1 <= len(content):
                        is_part = parse_line(content[i+1], first_index, int_length, spec_chars)
                    started_int = False
                    found_int = ""
                    first_index = 0
                    if is_part:
                        total += int(found_int)






