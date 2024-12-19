# %%

import numpy as np
import copy

input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def parse_input():
    input = {}
    # inputs/input_d7
    with open("test", "r") as f:
        for line in f.readlines():
            temp_split = line.split(": ")
            temp_list = temp_split[1].strip("\n").split(" ")
            temp_ints = [int(item) for item in temp_list]

            input[int(temp_split[0])] = temp_ints

    return input


def calc_options(my_vars):
    output = []
    input_list = copy.deepcopy(
        my_vars
    )  # stop this from deleting variables from the dictionary lists
    if len(input_list) == 2:
        output.append(input_list[0] + input_list[1])
        output.append(input_list[0] * input_list[1])
        output.append(int(str(input_list[0]) + str(input_list[1])))

    elif len(input_list) == 0:
        print("no values in the input list")
    else:
        new_list = np.array([])

        a = input_list.pop(0)
        b = input_list.pop(0)

        new_list = np.append(new_list, [a + b])
        new_list = np.append(new_list, [a * b])
        new_list = np.append(new_list, [int(str(a) + str(b))])

        while len(input_list) >= 1:
            c = input_list.pop(0)

            new_list = np.append(
                new_list + c, new_list * c, part2_concat(new_list, c)
            )  # part 1

        output = new_list

    return output


def evaluate_equations(key_val, input_list):
    values = calc_options(input_list)
    return key_val in values


def loop_input(my_dict):
    output = []

    for k, v in my_dict.items():
        if evaluate_equations(k, v):
            output.append(k)

    return output


def part2_concat(arr, concat_val):
    output = arr.astype(int)
    for idx, val in enumerate(output):
        output[idx] = int(str(val) + str(concat_val))

    return output


s = parse_input()

vals = loop_input(s)
print(vals)

print(f"Sum of correct inputs are: {sum(vals)}")

# %%
