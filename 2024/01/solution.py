def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data):
    left = list()
    right = list()
    for d in data:
        a = d.split()
        left.append(int(a[0]))
        right.append(int(a[1]))
    return zip(sorted(left), sorted(right))


def solve_part_1(data):
    parsed = parse_data(data)
    return sum([abs(a[0] - a[1]) for a in parsed])


def solve_part_2(data):
    parsed = parse_data(data)
    commonalities = dict()
    left = list()
    for p in parsed:
        left.append(p[0])
        v = p[1]
        if v not in commonalities:
            commonalities[v] = 0
        commonalities[v] += 1
    total = 0
    for p in left:
        total += p * commonalities.get(p, 0)
    return total


def part_1(data):
    total = solve_part_1(data)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = solve_part_2(data)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
