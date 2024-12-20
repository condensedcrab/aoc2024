s = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def parse_input():
    map = []
    # inputs/input_d7
    with open("test", "r") as f:
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


my_map = parse_input()
u = find_unique_chars(my_map)
print(u)
