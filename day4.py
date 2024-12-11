# %% define functions
import re


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
            print(s[idx : idx + 40 : 10])
            counts += 1
    return counts


def diagonal_search(s):
    counts = 0
    for idx, val in enumerate(s):
        if s[idx : idx + 40 : 10] in ["XMAS", "SAMX"]:
            print(s[idx : idx + 40 : 10])
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
