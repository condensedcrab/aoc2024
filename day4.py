# %% define functions
import re


def row_search():

    return None


def col_search():

    return None


def diagonal_search():

    return None


# %%

input_file = "test"

s = ""
with open(input_file, "r") as file:
    for row in file.readlines():
        s += row

print(s)

p = re.compile(r"(?:XMAS)| (?:SAMX)")

m = p.findall(s)
print(m)
