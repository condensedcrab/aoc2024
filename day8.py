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
        if val[0] >= 0 and val[0] < nrows and val[1] >= 0 and val[1] < ncols:
            clean_anodes.append(val)
    return clean_anodes


def calc_antinodes_part2(locations, my_map):
    anodes = []
    nrows = len(my_map)
    ncols = len(my_map[0])

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            delta_row = locations[j][0] - locations[i][0]
            delta_col = locations[j][1] - locations[i][1]

            for n in range(-40, 40):
                anodes.append(
                    [locations[i][0] - delta_row * n, locations[i][1] - delta_col * n]
                )
                anodes.append(
                    [locations[j][0] + delta_row * n, locations[j][1] + delta_col * n]
                )

    clean_anodes = []
    for idx, val in enumerate(anodes):
        if val[0] >= 0 and val[0] < nrows and val[1] >= 0 and val[1] < ncols:
            clean_anodes.append(val)
    return clean_anodes


def unique_locs(location_list):
    output = []

    for l in location_list:
        if l not in output:
            output.append(l)

    return output


# %% test region for part 1
my_map = parse_input("test")
u = find_unique_chars(my_map)
total_locs = []
for c in u:
    l = find_locs(c, my_map)
    a = calc_antinodes(l, my_map)
    total_locs += a


print(f"Total number of unique antinodes is: {len(unique_locs(total_locs))}")

# %% part 1
my_map = parse_input("inputs/input_d8")
u = find_unique_chars(my_map)

total_locs = []
for c in u:
    l = find_locs(c, my_map)
    a = calc_antinodes(l, my_map)
    total_locs += a


unq_loc = unique_locs(total_locs)

print(f"Total number of unique antinodes is: {len(unq_loc)}")

# %% part 2

my_map = parse_input("test")
u = find_unique_chars(my_map)

total_locs = []
for c in u:
    l = find_locs(c, my_map)
    a = calc_antinodes_part2(l, my_map)
    total_locs += a


unq_loc = unique_locs(total_locs)

print(f"Part2 test case: Total number of unique antinodes is: {len(unq_loc)}")
my_map = parse_input("inputs/input_d8")
u = find_unique_chars(my_map)

total_locs = []
for c in u:
    l = find_locs(c, my_map)
    a = calc_antinodes_part2(l, my_map)
    total_locs += a


unq_loc = unique_locs(total_locs)

print(f"Part 2 big kahuna: Total number of unique antinodes is: {len(unq_loc)}")
