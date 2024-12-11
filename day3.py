# %%
import re
import numpy

input_file = "input_d3"
p = re.compile(r"mul[(](\d+),(\d+)+[)]")
output = 0
with open(input_file, "r") as file:
    for row in file.readlines():
        # s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        s = row

        matches = p.findall(s)

        print(matches)

        for m in matches:
            output += int(m[0]) * int(m[1])

print(f"Total output is: {output}")
# %% part 2
clean_match = []
input_file = "input_d3"
p = re.compile(r"(mul[(]\d+,\d+[)])| ?(don't[(][)])| ?(do[(][)])")

output = 0
with open(input_file, "r") as file:
    for row in file.readlines():
        s = row
        matches = p.findall(s)

        # clean up the parsed results
        for m in matches:
            for phrase in m:
                if phrase != "":
                    clean_match.append(phrase)

# s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

print(clean_match)

# now implement algo
toggle_flag = True
output = 0
p = re.compile(r"(\d+),(\d+)")

# loop through found phrases and toggle the sum depending on whether it is enabled

for phrase in clean_match:
    if phrase == "don't()":
        toggle_flag = False
    elif phrase == "do()":
        toggle_flag = True

    if toggle_flag and "mul" in phrase:
        phrase_find = p.findall(phrase)
        for m in phrase_find:
            output += int(m[0]) * int(m[1])

print(f"total output is: {output}")
