# %%

import numpy as np

input_file = "input_d2"


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


# %%
