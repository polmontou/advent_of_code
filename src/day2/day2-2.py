file_path = "set.txt"
game_set = {"blue":14,"green":13,"red":12}
digits = [0,1,2,3,4,5,6,7,8,9]

def find_int_forward(text) :
    integer = ""
    founded_int_once = False

    for i in range(len(text)):
        digits_found = False
        for j, digit in enumerate(digits):
            if  str(digit) == text[i]:
                integer += text[i]
                digits_found = True
                founded_int_once = True
                break
        if founded_int_once:
            if not digits_found:
                break

    return int(integer)

def find_int_backward (text, index):
    int_backward = ""
    int_forward = ""
    i = index
    founded_int_once = False
    stop = False

    while i != -1 and not stop:
        digit_found = False

        for j, digit in enumerate(digits):
            if  str(digit) == text[i]:
                int_backward += text[i]
                digit_found = True
                founded_int_once = True
                break

        if founded_int_once:
            if not digit_found:
                stop = True
        i -= 1

    i = len(int_backward)-1
    while i != -1:
        int_forward += int_backward[i]
        i -=1

    return int(int_forward)



def find_biggest_color_draw(text, color_searched):
    biggest_color_draw = 0

    for i in range(len(text)):
        color_found = True

        for j, letter in enumerate(color_searched):
            if i+j < len(text) and text[i+j] != letter:
                color_found = False
        if color_found:
            corresponding_draw_value = find_int_backward(text, i)
            if corresponding_draw_value > biggest_color_draw:
                biggest_color_draw = corresponding_draw_value

    return biggest_color_draw


with open(file_path, 'r') as f:
    content = f.readlines()
    total_power = 0

    for line in content:
        biggest_blue = find_biggest_color_draw(line, "blue")
        biggest_green = find_biggest_color_draw(line, "green")
        biggest_red = find_biggest_color_draw(line, "red")

        total_power += biggest_blue * biggest_green * biggest_red

    print(total_power)