def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def print_grid(grid):
    print("\n".join([" ".join([g_i for g_i in g]) for g in grid]))


def move(x, y, d):
    if d == 0:
        x += 1
    elif d == 1:
        y += 1
    elif d == 2:
        x -= 1
    else:
        y -= 1

    return x, y


def is_oob(x, y, data):
    return x < 0 or x >= len(data[0]) or y < 0 or y >= len(data)


def scatter_light(data, energized_grid, start_x, start_y, start_d):
    # L 0
    # N 1
    # E 2
    # S 3

    commands = [[start_x, start_y, start_d]]

    while len(commands) > 0:
        command = commands.pop(0)
        x = command[0]
        y = command[1]
        d = command[2]

        if energized_grid[y][x][d] > 0:
            continue
        else:
            energized_grid[y][x][d] = 1

        op = data[y][x]
        if op == ".":
            x, y = move(x, y, d)
            if is_oob(x, y, data):
                continue
            else:
                commands.append([x, y, d])
        if op in ["\\", "/"]:
            # from south = 3
            # from north = 1

            if (op == "\\" and d == 0) or (op == "/" and d == 2):
                d = 1
                y = y + 1
            elif (op == "/" and d == 0) or (op == "\\" and d == 2):
                d = 3
                y -= 1
            elif (op == "\\" and d == 3) or (op == "/" and d == 1):
                d = 2
                x -= 1
            elif (op == "/" and d == 3) or (op == "\\" and d == 1):
                d = 0
                x += 1
            if is_oob(x, y, data):
                continue
            else:
                commands.append([x, y, d])

        elif op in ["|", "-"]:
            if (op == "|" and d in [1, 3]) or (op == "-" and d in [0, 2]):
                x, y = move(x, y, d)
                if is_oob(x, y, data):
                    continue
                commands.append([x, y, d])
            else:
                x_a = x
                x_b = x
                y_a = y
                y_b = y
                d_a = None
                d_a = None
                if op == "|" and d in [0, 2]:
                    y_a += 1
                    y_b -= 1
                    d_a = 1
                    d_b = 3
                elif op == "-" and d in [1, 3]:
                    x_a += 1
                    x_b -= 1
                    d_a = 0
                    d_b = 2

                if not is_oob(x_a, y_a, data):
                    commands.append([x_a, y_a, d_a])
                if not is_oob(x_b, y_b, data):
                    commands.append([x_b, y_b, d_b])
    return energized_grid


def get_score(energized_grid):
    total = 0

    for e in energized_grid:
        for v in e:
            if 1 in v:
                total += 1
    return total


def part_1(data):
    energized_grid = [[[0, 0, 0, 0] for d in d_i] for d_i in data]

    scatter_light(data, energized_grid, 0, 0, 0)
    total = get_score(energized_grid)

    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    for x in range(0, len(data[0])):
        for y in [0, len(data) - 1]:
            energized_grid = [[[0, 0, 0, 0] for d in d_i] for d_i in data]
            grid = scatter_light(data, energized_grid, x, y, 1 if y == 0 else 3)
            res = get_score(grid)
            total = max(res, total)

    for y in range(0, len(data)):
        for x in [0, len(data[0]) - 1]:
            energized_grid = [[[0, 0, 0, 0] for d in d_i] for d_i in data]
            grid = scatter_light(data, energized_grid, x, y, 0 if x == 0 else 2)
            res = get_score(grid)
            total = max(res, total)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
