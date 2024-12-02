def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def solve_part_1(data):

    total = 0
    for row, d in enumerate(data):
        v = [int(i) for i in d.strip().split()]
        good = True
        decreasing = (v[1] - v[0]) < 0
        if v[1] - v[0] == 0:
            continue
        for i in range(0, len(v) - 1):
            this_d = v[i + 1] - v[i]
            if (this_d < 0) != decreasing or this_d == 0 or abs(this_d) > 3:
                good = False
                break

        if good:
            total += 1
    return total


def row_is_good(v):
    good = True
    decreasing = (v[1] - v[0]) < 0
    if v[1] - v[0] == 0:
        return False
    for i in range(0, len(v) - 1):
        this_d = v[i + 1] - v[i]
        if (this_d < 0) != decreasing or this_d == 0 or abs(this_d) > 3:
            good = False
            break

    return good


def solve_part_2(data):
    total = 0
    for row, d in enumerate(data):
        dat = [int(i) for i in d.strip().split()]
        good = row_is_good(dat)
        for i in range(len(dat)):
            good = good or row_is_good([d_i for i_, d_i in enumerate(dat) if i_ != i])
            if good:
                break

        total += 1 if good else 0
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
