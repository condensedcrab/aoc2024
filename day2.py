# %% day2a

import numpy as np


# define functions
def check_signs(x):
    difference = np.diff(x)
    sign_diff = np.abs(np.sign(difference).sum()) == len(x) - 1

    return sign_diff


def check_signs_damp(x):
    sign_diff = check_signs(x)
    z = x.copy()
    if not sign_diff:
        for idx, val in enumerate(x):
            y = x.copy()
            y.pop(idx)
            if check_signs(y):
                sign_diff = True
                z = y.copy()
                break

    return [sign_diff, z]


def check_gap(x):
    difference = np.diff(x)
    gap_size = np.all(np.logical_and(np.abs(difference) >= 1, np.abs(difference) <= 3))

    return gap_size


def check_gap_damp(x):
    gap_size = check_gap(x)
    z = x.copy()
    if not gap_size:
        for idx, val in enumerate(x):
            y = x.copy()
            y.pop(idx)
            if check_gap(y):
                gap_size = True
                z = y.copy()
                break

    return [gap_size, z]


# %% day 2a
input_file = "test"
input_file = "inputs/input_d2"

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

# input_file = "test"
input_file = "input_d2"
counter = 0
with open(input_file, "r") as file:
    for row in file.readlines():
        l = row.split((" "))
        x = [int(a) for a in l]

        sign_check = check_signs(x)
        gap_check = check_gap(x)

        if sign_check and gap_check:
            counter += 1
        else:
            for idx, val in enumerate(x):
                y = x.copy()
                y.pop(idx)

                sign_check = check_signs(y)
                gap_check = check_gap(y)

                if sign_check and gap_check:
                    counter += 1
                    break


print(f"Total number of safe reports is: {counter}")
