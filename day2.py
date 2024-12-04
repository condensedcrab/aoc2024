# %% day2a

import numpy as np


# define functions
def check_signs(x):
    difference = np.diff(x)
    sign_diff = np.abs(np.sign(difference).sum()) == len(x) - 1

    return sign_diff


def check_signs_damp(x):
    sign_diff = check_signs(x)
    if not sign_diff:
        for idx, val in enumerate(x):
            y = x.copy()
            y.pop(idx)
            if check_signs(y):
                sign_diff = True
                break

    return sign_diff


def check_gap(x):
    difference = np.diff(x)
    gap_size = np.all(np.logical_and(np.abs(difference) >= 1, np.abs(difference) <= 3))

    return gap_size


def check_gap_damp(x):
    gap_size = check_gap(x)
    if not gap_size:
        for idx, val in enumerate(x):
            y = x.copy()
            y.pop(idx)
            if check_gap(y):
                gap_size = True
                break

    return gap_size


# %% day 2a
input_file = "test"
input_file = "input_d2"

counter = 0
with open(input_file, "r") as file:
    for row in file.readlines():
        l = row.split((" "))
        x = [int(a) for a in l]

        print(f"Input list is: {x}")

        sign_check = check_signs(x)
        print(f"Sign of change is correct: {sign_check}")

        gap_check = check_gap(x)
        print(f"Magnitude of change is correct: {gap_check}")

        if gap_check and sign_check:
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

        damp_sign = check_signs_damp(x)
        print(f"Dampened sign of change is correct: {damp_sign }")

        damp_gap = check_gap_damp(x)
        print(f"Magnitude of change is correct: {damp_gap}")

        if damp_sign and damp_gap:
            counter += 1

print(f"Total number of safe reports is: {counter}")
