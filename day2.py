# %% day2a

import numpy as np

input_file = "test"
input_file = "input_d2"

counter = 0
with open(input_file, "r") as file:
    for row in file.readlines():
        l = row.split((" "))
        x = [int(a) for a in l]

        print(f"Input list is: {x}")

        difference = np.diff(x)
        sign_diff = np.abs(np.sign(difference).sum()) == len(x) - 1
        print(f"All decreasing or increasing: {sign_diff}")

        gap_size = np.all(
            np.logical_and(np.abs(difference) >= 1, np.abs(difference) <= 3)
        )
        print(f"Gap size satifies requirements within [1,3]: {gap_size}")

        if gap_size and sign_diff:
            counter += 1

print(f"Total number of safe reports is: {counter}")
# %% day2b
input_file = "test"
# input_file = "input_d2"

counter = 0
with open(input_file, "r") as file:
    for row in file.readlines():
        l = row.split((" "))
        x = [int(a) for a in l]

        print(f"Input list is: {x}")

        sign_diff = check_signs(x)
        gap_check = check_gap(x)

        if gap_size and sign_diff:
            counter += 1

print(f"Total number of safe reports is: {counter}")


# %% define functions


def check_signs(x):
    difference = np.diff(x)
    sign_diff = np.abs(np.sign(difference).sum()) == len(x) - 1

    return sign_diff


def check_gap(x):
    difference = np.diff(x)
    gap_size = np.all(np.logical_and(np.abs(difference) >= 1, np.abs(difference) <= 3))


# %%
