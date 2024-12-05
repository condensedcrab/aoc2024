# %%
import re
import numpy

s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

p = re.compile(r"mul[(](\d+),(\d)+[)]")
matches = p.findall(s)

print(matches)

output = 0
for m in matches:
    output += int(m[0]) * int(m[1])

print(f"Total output is: {output}")
