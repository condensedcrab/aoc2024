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

# %%

inputFile = open("inputs/input_d8", "r")
input = inputFile.readlines()
inputFile.close()

for line in input:
    input[input.index(line)] = line.replace("\n", "")

# The variable "output" is what will be printed
output = ""

# Calculate amount of antinodes
characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
antinodes = []

for c in range(len(characters)):
    i = characters[c]
    loc = []
    for line in range(len(input)):
        y = input[line]
        for column in range(len(y)):
            x = y[column]
            if x == i:
                loc.append([column, line])

    for o in range(len(loc)):
        for t in range(len(loc)):
            if o == t:
                continue

            x1 = loc[o][0]
            y1 = loc[o][1]
            x2 = loc[t][0]
            y2 = loc[t][1]

            dx = x2 - x1
            dy = y2 - y1

            antinodes.append([x1 - dx, y1 - dy])

# Remove duplicates and out-of-bounds antinodes
final = []

for i in antinodes:
    if (
        i not in final
        and i[0] >= 0
        and i[1] >= 0
        and i[0] + 1 <= len(input)
        and i[1] + 1 <= len(input[0])
    ):
        final.append(i)

output = len(final)

# Print the output
print(output)

# %% compare

for ele in unq_loc:
    flag_found = False

    for l in final:
        if ele == output:
            flag_found = True
            break

    if not flag_found:
        print(ele)
