# %%

import numpy as np

input_file = "input_d2"


with open(input_file, "r") as file:
    for row in file.readlines():
        l = row.split((" "))
        x = [int(a) for a in l]

        print(f"Input list is: {x}")

        difference = np.diff(x)
        print(f"Adjacent diff is: {difference}")
        sign_diff = np.diff(np.sign(difference)).sum() == 0
        print("All decreasing or increasing: {sign_diff}")


# %%
