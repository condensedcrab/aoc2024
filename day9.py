s = "2333133121414131402"
# s = "12345"
import numpy as np


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


def convert_to_np(s):
    output = np.zeros(len(s))
    for idx, val in enumerate(s):
        if val == ".":
            output[idx] = np.nan
        else:
            output[idx] = int(val)

    return output


def first_dot(my_str):
    b = np.where(np.isnan(my_str))
    return np.min(b)


def last_digit(my_str):
    b = np.where(~np.isnan(my_str))
    return np.max(b)


def move_files(my_str):
    counter = 0
    while first_dot(my_str) < last_digit(my_str):
        idx_dot = first_dot(my_str)
        idx_num = last_digit(my_str)

        value = my_str[idx_num]
        my_str[idx_num] = np.nan
        my_str[idx_dot] = value

        counter += 1
        if counter % 500 == 0:
            print(f"Iteration: {counter}")

        # print(my_str)

    return my_str


def first_dot_chunk(my_str):
    b = np.where(np.isnan(my_str))
    return np.min(b)


def move_chunks(my_str):
    counter = 0
    while first_dot(my_str) < last_digit(my_str):
        idx_dot = first_dot(my_str)
        idx_num = last_digit(my_str)

        value = my_str[idx_num]
        my_str[idx_num] = np.nan
        my_str[idx_dot] = value

        counter += 1
        if counter % 500 == 0:
            print(f"Iteration: {counter}")

        # print(my_str)

    return my_str


def calc_checksum(data):
    output = 0
    for idx, val in enumerate(data):
        if np.isnan(val):
            continue

        output += idx * val

    return output


# %% part 1
s = ""
with open("inputs/input_d9", "r") as f:
    for line in f.readlines():
        s = s.join(line)

a = unwrap(s)

d = convert_to_np(a)
b = move_files(d)
c = calc_checksum(b)

print(f"Checksum is: {c}")

# %% part 2

s = "2333133121414131402"
a = unwrap(s)
d = convert_to_np(a)
