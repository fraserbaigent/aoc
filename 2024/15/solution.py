def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data, is_part_2=False):
    grid = []
    instructions = None

    for i, d in enumerate(data):
        if len(d) == 0:
            instructions = "".join(data[i:]).replace("\n", "")
            break
        else:
            if is_part_2 == True:
                d = (
                    d.replace("#", "##")
                    .replace("O", "[]")
                    .replace(".", "..")
                    .replace("@", "@.")
                )

            grid.append([c for c in d])

    return grid, instructions


def find_start(grid):
    for y, g in enumerate(grid):
        for x, c in enumerate(g):
            if grid[y][x] == "@":
                return x, y
    return None, None


DIRS = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}


def move(x, y, direction, grid):
    dx, dy = DIRS[direction]
    nx = x + dx
    ny = y + dy
    if grid[ny][nx] == ".":
        grid[ny][nx] = grid[y][x]
        if grid[y][x] == "@":
            grid[y][x] = "."
        return nx, ny
    elif grid[ny][nx] == "#":
        return x, y
    elif grid[ny][nx] == "O" or grid[ny][nx] in "[]":
        nnx, nny = move(nx, ny, direction, grid)
        if nnx == nx and nny == ny:
            return x, y
        else:
            grid[ny][nx] = grid[y][x]
            if grid[y][x] == "@":
                grid[y][x] = "."
            return nx, ny


def get_score(grid, is_part_2=False):
    total = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "O" or (is_part_2 and c == "["):
                v = (y * 100) + x
                total += v
    return total


def solve_part_1(data):
    grid, instructions = parse_data(data)
    x, y = find_start(grid)
    for c in instructions:
        x, y = move(x, y, c, grid)
    return get_score(grid)


def move_2(x, y, direction, grid):
    dx, dy = DIRS[direction]
    if dy == 0:
        x, y = move(x, y, direction, grid)
        return x, y
    else:
        valid_moves = move_2_vertical(x, y, direction, grid)
        if len(valid_moves) == 0:
            return x, y
        visited = []
        for (x_f, y_f), (x_t, y_t), c in valid_moves:
            grid[y_t][x_t] = c
            visited.append((x_t, y_t))
        for c_from, _, _ in valid_moves:
            if c_from not in visited:
                x_f, y_f = c_from
                grid[y_f][x_f] = "."

        return x, y + dy


def move_2_vertical(x, y, direction, grid):
    dx, dy = DIRS[direction]
    ny = y + dy
    if grid[ny][x] == "#":
        return []
    elif grid[ny][x] == ".":
        return [((x, y), (x, ny), grid[y][x])]

    if grid[ny][x] == "[":
        nx = x + 1
    elif grid[ny][x] == "]":
        nx = x - 1
    else:
        raise Exception(f"WTF - {x}, {ny} is {grid[ny][x]}")
    valid = [((x, y), (x, ny), grid[y][x])]
    for x_i in [x, nx]:
        next_row = move_2_vertical(x_i, ny, direction, grid)
        if len(next_row) == 0:
            return []
        else:
            for n in next_row:
                valid.append(n)

    return valid


def solve_part_2(data):
    grid, instructions = parse_data(data, True)
    x, y = find_start(grid)
    for i, c in enumerate(instructions):
        x, y = move_2(x, y, c, grid)
    return get_score(grid, True)


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
