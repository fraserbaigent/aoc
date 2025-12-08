from AocCommon import data_to_list_grid, get_data, get_data_blob, split_data_with_regex


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")
# data = get_data_blob()
data = data_to_list_grid(data)
# data = split_data_with_regex(data, "add pattern")

##########################################################################


def solve_part_1(grid):
    total = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if grid[y][x] != "@":
                continue
            cnt = 0
            for xx in range(x - 1, x + 2):
                if xx < 0 or xx >= len(row):
                    continue
                for yy in range(y - 1, y + 2):
                    if yy < 0 or yy >= len(grid) or grid[yy][xx] != "@":
                        continue
                    cnt += 1
            if cnt <= 4:
                total += 1
    return total


def solve_part_2(grid):
    total = 0
    to_remove = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if grid[y][x] != "@":
                continue
            cnt = 0
            for xx in range(x - 1, x + 2):
                if xx < 0 or xx >= len(row):
                    continue
                for yy in range(y - 1, y + 2):
                    if yy < 0 or yy >= len(grid) or grid[yy][xx] != "@":
                        continue
                    cnt += 1
            if cnt <= 4:
                total += 1
                to_remove.append((x, y))
    return to_remove


def part_1(data):
    total = solve_part_1(data)

    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    while True:
        to_remove = solve_part_2(data)
        total += len(to_remove)
        if len(to_remove) == 0:
            break
        for x, y in to_remove:
            data[y][x] = "."

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
