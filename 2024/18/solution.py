import copy


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################

DIRS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]


def solve_part_1(data):
    width = 71
    height = 71
    grid = [["." for i in range(0, width)] for j in range(0, height)]
    coords = [(int(x[0]), int(x[1])) for x in [d.split(",") for d in data]]
    for x, y in coords[:1024]:
        #        print(y, x)
        grid[y][x] = "#"
    # print("\n".join(["".join(g) for g in grid]))

    cache = [[None for g in g_] for g_ in grid]

    start = ((0, 0), 0)
    steps = [start]
    while len(steps):
        (x, y), score = steps.pop(0)
        if cache[y][x] is not None and cache[y][x] <= score or grid[y][x] == "#":
            continue
        cache[y][x] = score
        next_score = score + 1
        for dx, dy in DIRS:
            xn = x + dx
            yn = y + dy
            if xn < 0 or yn < 0 or xn >= len(grid[0]) or yn >= len(grid):
                continue
            steps.append(((xn, yn), next_score))
    return cache[-1][-1]


def solve_with_grid(grid):
    cache = [[None for g in g_] for g_ in grid]

    start = ((0, 0), 0)
    steps = [start]
    while len(steps):
        (x, y), score = steps.pop(0)
        if cache[y][x] is not None and cache[y][x] <= score or grid[y][x] == "#":
            continue
        cache[y][x] = score
        next_score = score + 1
        for dx, dy in DIRS:
            xn = x + dx
            yn = y + dy
            if xn < 0 or yn < 0 or xn >= len(grid[0]) or yn >= len(grid):
                continue
            steps.append(((xn, yn), next_score))
    return cache[-1][-1]


def solve_part_2(data):
    width = 71
    height = 71
    grid = [["." for i in range(0, width)] for j in range(0, height)]
    coords = [(int(x[0]), int(x[1])) for x in [d.split(",") for d in data]]
    min_data_o = 1024
    for x, y in coords[:min_data_o]:
        grid[y][x] = "#"
    max_data = len(coords)
    min_data = min_data_o
    grid_n = copy.deepcopy(grid)
    for i in range(min_data_o, len(coords)):
        x, y = coords[i]
        grid_n[y][x] = "#"
        result = solve_with_grid(grid_n)
        if result is None:
            break
    return f"{coords[i][0]},{coords[i][1]}"


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
