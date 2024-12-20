s = "2333133121414131402"
s = "12345"


def unwrap(s):
    output = []
    id = 0
    for idx, val in enumerate(s):
        if idx % 2 == 0:
            for n in range(0, int(val)):
                output.append(str(id))
            id += 1
        else:
            for n in range(0, int(val)):
                output.append(".")

    return "".join(output)


print(unwrap(s))
