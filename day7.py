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


def parse_input(file):
    input = {}
    with open("inputs/input_d7", "r") as f:
        for line in f.readlines():
            temp_split = line.split(": ")
            input[temp_split[0]]: temp_split[1]


def calc_options(input_list):
    output = np.array([]) # we are going to be changing these arrays a bunch but they're small
    my_list = copy.deepcopy(input_list)

    while len(my_list) >= 2:
        a = my_list.pop(0)
        b = my_list.pop(0)
        if len(output) == 0:
            output.append(a+b)
            output.append(a*b)
        else:
            for ele in output:
                


calc_options([10, 19])
calc_options([16, 10, 13])

# %%
