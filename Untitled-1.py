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
