from AocCommon import data_to_list_grid, get_data, get_data_blob, split_data_with_regex


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.replace("\n", "") for l in infile.readlines()]


data = get_data("data.dat")
# data = get_data_blob()
# data = data_to_list_grid()
# data = split_data_with_regex(data, "add pattern")

##########################################################################


def solve_part_1(data):
    vals = [[] for i in data[0].split()]
    for i, d in enumerate(data[:-1]):
        for j, dd in enumerate(d.split()):
            vals[j].append(int(dd))

    total = 0

    for i, op in enumerate(data[-1].split()):
        if op == "+":
            total += sum(vals[i])
        elif op == "*":
            v = 1
            for v_i in vals[i]:
                v *= v_i
            total += v
        else:
            raise ValueError("Whoops")
    return total


def solve_part_2(data):
    total = 0
    vals = []
    op = None
    i = 0
    for x in range(len(data[0]) - 1, -1, -1):
        i += 1
        chars = []

        for y in range(0, len(data)):
            c = data[y][x]
            if c == " ":
                continue
            elif c in "*+":
                op = c
            else:
                chars.append(c)
        if len(chars) != 0:
            num = int("".join(chars))
            vals.append(num)
        if op is not None:
            if op == "+":
                total += sum(vals)
            elif op == "*":
                v = 1
                for v_i in vals:
                    v *= v_i
                total += v
            vals = []
            op = None

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
