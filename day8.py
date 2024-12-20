# %%


def parse_input(filename):
    map = []
    # inputs/input_d7
    with open(filename, "r") as f:
        for line in f.readlines():
            map.append(list(line.replace("\n", "")))

    return map


def find_unique_chars(map):
    output = []
    for row in map:
        s = set(row)
        for ele in s:
            if ele == ".":
                continue
            elif s in output:
                continue
            else:
                output.append(ele)

    return list(set(output))


def find_locs(my_char, char_map):
    locs = []

    for row_idx, row in enumerate(char_map):
        try:
            col_idx = row.index(my_char)
            locs.append([row_idx, col_idx])

        except:
            pass

    return locs


def calc_antinodes(locations, my_map):
    anodes = []
    nrows = len(my_map)
    ncols = len(my_map[0])

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            delta_row = locations[j][0] - locations[i][0]
            delta_col = locations[j][1] - locations[i][1]

            anodes.append([locations[i][0] - delta_row, locations[i][1] - delta_col])
            anodes.append([locations[j][0] + delta_row, locations[j][1] + delta_col])

    clean_anodes = []
    for idx, val in enumerate(anodes):
        if not (val[0] < 0 or val[0] > nrows or val[1] < 0 or val[1] > ncols):
            clean_anodes.append(val)
    return clean_anodes


# %% test region
my_map = parse_input("test")
u = find_unique_chars(my_map)
print(u)

l = find_locs("A", my_map)
print(l)

a = calc_antinodes(l, my_map)
print(a)

answer = parse_input("test2")
