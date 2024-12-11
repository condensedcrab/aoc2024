# %% define functions
from operator import itemgetter


def row_search(s):
    counts = 0
    for idx, val in enumerate(s):
        if s[idx : idx + 4] in ["XMAS", "SAMX"]:
            counts += 1
    return counts


def col_search(s):
    counts = 0
    row_size = 11
    for idx, val in enumerate(s):
        if s[idx : idx + 40 : row_size] in ["XMAS", "SAMX"]:
            print(s[idx : idx + 40 : row_size])
            counts += 1
    return counts


def diagonal_search(s):
    counts = 0
    for idx, val in enumerate(s):

        # check if downward diagonal fits within row and column borders
        # if divmod(idx, 10)[0] >= divmod(len(s), 10)[0] - 3:
        #     continue
        if divmod(idx, 11)[1] > 6:
            continue
        if idx > 50:
            break

        # construct diagonal
        row_size = 11
        test_str = ""
        for i in range(0, 4):
            test_str += s[idx + (row_size * i) + i]

        print(test_str)

        if test_str in ["XMAS", "SAMX"]:
            counts += 1
    return counts


# %%

input_file = "test"

s = ""
with open(input_file, "r") as file:
    for row in file.readlines():
        s += row

# print(s)
row_search(s)
col_search(s)
diagonal_search(s)

# format is 9 letters with a '\n' char
