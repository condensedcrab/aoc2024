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
        # check that we don't overrun the number of rows
        if divmod(idx, 10)[0] > divmod(len(s), 10)[0] - 4:
            continue

        # check column position so we don't overrun columns into the newline char
        if divmod(idx, 11)[1] > 6:
            continue

        # construct diagonal
        row_size = 11
        test_str = ""
        for i in range(0, 4):
            test_str += s[idx + (row_size * i) + i]

        print(test_str)

        if test_str in ["XMAS", "SAMX"]:
            print(f"Found match: {test_str}. Count is: {counts}")
            counts += 1
    return counts


def antidiagonal_search(s):
    counts = 0
    for idx, val in enumerate(s):
        # check that we don't overrun the number of rows
        if divmod(idx, 10)[0] > divmod(len(s), 10)[0] - 4:
            continue

        # check column position so we don't overrun columns into the newline char
        if divmod(idx, 11)[1] > 6:
            continue

        # construct diagonal
        row_size = 11
        test_str = ""
        for i in range(0, 4):
            test_str += s[idx + (row_size * i) + i]

        print(test_str)

        if test_str in ["XMAS", "SAMX"]:
            print(f"Found match: {test_str}. Count is: {counts}")
            counts += 1
    return counts


# %%

input_file = "test"

s = ""
with open(input_file, "r") as file:
    for row in file.readlines():
        s += row

# print(s)
total_counts = row_search(s) + col_search(s) + diagonal_search(s)

print(f"Total instances of XMAS found: {total_counts}")
# format is 9 letters with a '\n' char
