def splitlines(data):
    return [(v[0], int(v[1:])) for v in data]


def part_2(data):
    vals = splitlines(data)
    dirs = {"L": -1, "R": 1}

    i = 50
    total = 0
    for d, v in vals:
        old_i = i
        i += dirs[d] * v
        i %= 100
        if i == 0:
            if i != old_i:
                total += 1
        elif d == "L" and i > old_i and old_i != 0:
            total += 1
        elif d == "R" and i < old_i:
            total += 1
        total += v // 100

    print(total)
    return total


if __name__ == "__main__":
    with open("data.dat", "r") as infile:
        vals = infile.readlines()

    part_2(vals)
