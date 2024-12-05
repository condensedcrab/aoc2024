# %%
import re
import numpy

s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

p = re.compile(r"mul[(](\d+),(\d)+[)]")
matches = p.findall(s)

print(matches)

p2 = re.compile(r"\d+,\d+")

# for m in matches:
