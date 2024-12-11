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
    for idx, val in enumerate(s):
        if s[idx : idx + 40 : 10] in ["XMAS", "SAMX"]:
            counts += 1
    return counts


def diagonal_search(s):
    counts = 0
    for idx, val in enumerate(s):

        # check if downward diagonal fits within row and column borders
        # if divmod(idx, 10)[0] >= divmod(len(s), 10)[0] - 3:
        #     continue
        # if divmod(idx, 10)[1] > 6:
        #     continue
        if idx > 50:
            break
        test_str = val + s[idx + 11] + s[idx + 12] + s[idx + 13]
        if r"\n" in test_str:
            continue
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

print(s)

# format is 9 letters with a '\n' char
