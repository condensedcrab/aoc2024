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
    with open("inputs/input_d7", "r") as f:
        for line in f.readlines():
            temp_split = line.split(": ")
            temp_list = temp_split[1].strip("\n").split(" ")
            temp_ints = [int(item) for item in temp_list]

            input[int(temp_split[0])] = temp_ints

    return input


def calc_options(input_list):
    output = []

    if len(input_list) == 2:
        output.append(input_list[0] + input_list[1])
        output.append(input_list[0] * input_list[1])
    else:
        new_list = np.array([])

        a = input_list.pop(0)
        b = input_list.pop(0)

        new_list = np.append(new_list, [a + b])
        new_list = np.append(new_list, [a * b])

        while len(input_list) >= 1:
            c = input_list.pop(0)
            new_list = np.append(new_list + c, new_list * c)

        output = new_list

    return output


def evaluate_equations(key_val, input_list):
    values = calc_options(input_list)
    return key_val in values


print(calc_options([10, 19]))
print(calc_options([81, 40, 27]))
print(calc_options([11, 6, 16, 20]))

evaluate_equations(51, [10, 19])

s = parse_input()

# %%
