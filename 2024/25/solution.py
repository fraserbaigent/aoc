from AocCommon import get_data_blob


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data_blob()

##########################################################################


def parse(data):
    keys = []
    locks = []
    for k in data.split("\n\n"):
        lines = [k_.strip() for k_ in k.split("\n") if k_.strip() != ""]
        is_key = "." in lines[0]
        height = [0 for i in lines[0]]
        for l in lines[1:-1]:
            for i, l_ in enumerate(l):
                if l_ == "#":
                    height[i] += 1
        if is_key:
            keys.append(height)
        else:
            locks.append(height)
    return keys, locks


def fits(key, lock):
    for i, k in enumerate(key):
        if k + lock[i] > 5:
            return False
    return True


def get_total(keys, locks):
    total = 0
    for l in locks:
        for k in keys:
            if fits(k, l):
                total += 1
    return total


def solve_part_1(data):
    keys, locks = parse(data)
    total = get_total(keys, locks)
    return total


def solve_part_2(data):
    pass


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
