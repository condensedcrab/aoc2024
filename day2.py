# %%

import numpy as np

input_file = "input_d2"


with open(input_file, "r") as file:
    for row in file.readlines():
        l = row.split((" "))
        x = [int(a) for a in l]

        print(x)


# %%
