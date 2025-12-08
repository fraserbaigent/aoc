from copy import deepcopy

from AocCommon import data_to_list_grid, get_data, get_data_blob, split_data_with_regex


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")
data = data_to_list_grid(data)

##########################################################################


def get_start(data_0):
    for i in range(0, len(data_0)):
        if data_0[i] == "S":
            return i


def fire_laser(data):
    next_steps = []
    been = set()
    start = get_start(data[0])
    next_steps.append((start, 0))
    splits = 0
    while len(next_steps):
        x, y = next_steps.pop(0)
        if (x, y) in been:
            continue
        been.add((x, y))
        if x < 0 or x >= len(data[0]) or y >= len(data):
            continue
        c = data[y][x]
        if c == "^":
            splits += 1
            next_steps.append((x - 1, y + 1))
            next_steps.append((x + 1, y + 1))
        else:
            data[y][x] = "|"
            next_steps.append((x, y + 1))
    return splits


def solve_part_1(data):
    splits = fire_laser(data)
    return splits


def solve_recursively(x, y, data, memo):
    yn = y + 1
    if yn >= len(data):
        return 1
    elif (x, y) in memo:
        return memo[(x, y)]
    total_paths = 0
    if data[yn][x] == "^":
        total_paths += solve_recursively(x - 1, yn, data, memo)
        total_paths += solve_recursively(x + 1, yn, data, memo)
    else:
        total_paths += solve_recursively(x, yn, data, memo)
    memo[(x, y)] = total_paths
    return total_paths


def solve_part_2(data):
    start = get_start(data[0])
    return solve_recursively(start, 0, data, {})


def part_1(data):
    total = solve_part_1(deepcopy(data))
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = solve_part_2(data)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
