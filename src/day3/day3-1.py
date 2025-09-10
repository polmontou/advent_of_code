import re

file_path = "set.txt"
matrice = []

# with open(file_path, 'r') as f:
#     content = f.readlines()
#     for line in content:
#         chars_in_line = []
#         for char in line:
#             chars_in_line.append(char)
#         matrice.append(chars_in_line)
#
# find_spec_chars_patter = r""
#
# for line in matrice:
#     for char in line:
#         if re.match(spec_chars_pattern, char):
#             line_index = matrice.index(line)
#             char_index = line.index(char)
#             print("matrice[",line_index,"][",char_index,"]")