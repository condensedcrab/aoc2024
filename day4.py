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
    row_size = s.find('\n')+1
    for idx, val in enumerate(s):
        if s[idx : idx + 4*row_size : row_size] in ["XMAS", "SAMX"]:
            counts += 1

    print(f"Col found: {counts}")
    return counts


def diagonal_search(s):
    counts = 0
    row_size = s.find('\n')+1
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
        
        # construct antidiagonal
        test_str = ""
        for i in range(0, 4):
            test_str += s[idx + i * (row_size - 1)]
            
        if test_str in ["XMAS", "SAMX"]:
            counts += 1


    print(f"Diagonals found: {counts}")
    return counts

def xmas_search(s):
    counts = 0
    row_size = s.find('\n')+1
    
    for idx, val in enumerate(s):
        # check that we don't overrun the number of rows
        if idx + 2*(row_size + 1) >= len(s) or idx + 2*(row_size - 1) < 0:
            continue
        
        test_str = ["",""]
        for i in range(0, 3):
            test_str[0] += s[idx + i * (row_size + 1)]
            test_str[1] += s[idx + i * (row_size - 1)]
            
        if test_str[0] in ["MAS", "SAM"] and test_str[1] in ["MAS", "SAM"]:
            counts += 1
        
    print(f"X-mases found: {counts}")
    return counts


print(f"\n\n\nTest Case: ")
input_file = "test"

s = ""
with open(input_file, "r") as file:
    for row in file.readlines():
        s += row

# print(s)
total_counts = (
    row_search(s) + col_search(s) + diagonal_search(s)
)

xmas_counts = xmas_search(s)
print(f"Total instances of XMAS found: {total_counts}")
print(f"Total X-Mases found: {xmas_counts}")


print(f"\n\n\nInput File: ")
input_file = "input_d4"

s = ""
with open(input_file, "r") as file:
    for row in file.readlines():
        s += row

# print(s)
total_counts = (
    row_search(s) + col_search(s) + diagonal_search(s)
)

# xmas_counts = xmas_search(s)
print(f"Total instances of XMAS found: {total_counts}")
print(f"Total X-Mases found: {xmas_counts}")

