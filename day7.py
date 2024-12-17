import numpy

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

    output = []

    if len(input_list) == 2:
        output.append(input_list[0] + input_list[1])
        output.append(input_list[0] * input_list[1])

    return output


calc_options([10, 19])
