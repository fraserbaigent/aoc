def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def solve_part_1(instructions, string, index, cache):
    total = 0
    if string[index:] in cache:
        return cache[string[index:]]

    for i in instructions:
        if index + len(i) - 1 >= len(string):
            continue
        substr = string[index : index + len(i)]
        if substr == i:
            if index + len(i) == len(string):
                total += 1
            else:
                total += solve_part_1(instructions, string, index + len(i), cache)
    cache[string[index:]] = total
    return total


def solve_part_2(data):
    pass


def part_1(data):
    instructions = data[0].split(", ")
    total = 0
    for d in data[2:]:
        t = solve_part_1(instructions, d, 0, {})
        if t > 0:
            total += 1
    print(f"Part 1: {total}")
    return total


def part_2(data):
    instructions = data[0].split(", ")
    total = 0
    for d in data[2:]:
        total += solve_part_1(instructions, d, 0, {})

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
