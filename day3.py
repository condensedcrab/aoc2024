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

input_file = "input_d3"
# p = re.compile(r"mul[(](\d+),(\d+)+[)]")
output = 0
# with open(input_file, "r") as file:
#     for row in file.readlines():
# s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
p = re.compile(r"(mul[(]\d+,\d+[)])|(don't[()])| (do[()])")

s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

matches = p.findall(s)
print(matches)

# clean up the parsed results

clean_match = []
for m in matches:
    for phrase in m:
        if phrase != "":
            clean_match.append(phrase)
