s = "2333133121414131402"
# s = "12345"


def unwrap(s):
    output = []
    id = 0
    for idx, val in enumerate(s):
        if idx % 2 == 0:
            for n in range(0, int(val)):
                output.append(str(id))
            id += 1
        else:
            for n in range(0, int(val)):
                output.append(".")

    return output


def first_dot(my_str):
    return my_str.index(".")


def last_digit(my_str):
    first_digit = 0
    for idx, val in enumerate(my_str):
        if val.isdigit() and idx > first_digit:
            first_digit = idx

    return first_digit


def move_files(my_str):
    while first_dot(my_str) < last_digit(my_str):
        idx_dot = first_dot(my_str)
        idx_num = last_digit(my_str)

        value = my_str[idx_num]
        my_str[idx_num] = "."
        my_str[idx_dot] = value

        print(my_str)

    return my_str


def calc_checksum(data):
    output = []

    return output


a = unwrap(s)
b = move_files(a)

print(b)
