# %% define functions
from operator import itemgetter


def row_search(s):
    counts = 0
    for idx, val in enumerate(s):
        if s[idx : idx + 4] in ["XMAS", "SAMX"]:
            counts += 1

    print(f"Row found: {counts}")
    return counts


def col_search(s):
    counts = 0
    row_size = 11
    for idx, val in enumerate(s):
        if s[idx : idx + 4*row_size : row_size] in ["XMAS", "SAMX"]:
            counts += 1

    print(f"Col found: {counts}")
    return counts


def diagonal_search(s):
    counts = 0
    row_size = 11
    for idx, val in enumerate(s):

        # check that we don't overrun the number of rows
        if idx + 3*(row_size + 1) >= len(s):
            continue

        # construct diagonal
        test_str = ""
        for i in range(0, 4):
            test_str += s[idx + i * (row_size + 1)]

        if test_str in ["XMAS", "SAMX"]:
            counts += 1

    print(f"Diag found: {counts}")
    return counts


def antidiagonal_search(s):
    counts = 0
    row_size = 11
    
    for idx, val in enumerate(s):
        # check that we don't overrun the number of rows
        if idx + 3*(row_size + 1) >= len(s):
            continue

        # construct diagonal

        test_str = ""
        for i in range(0, 4):
            test_str += s[idx + i * (row_size + 1)]
        if test_str in ["XMAS", "SAMX"]:
            counts += 1

    print(f"Antidiag found: {counts}")
    return counts


# %%

input_file = "test"

s = ""
with open(input_file, "r") as file:
    for row in file.readlines():
        s += row

# print(s)
total_counts = (
    row_search(s) + col_search(s) + diagonal_search(s) + antidiagonal_search(s)
)

print(f"Total instances of XMAS found: {total_counts}")
# format is 9 letters with a '\n' char
