from AocCommon import data_to_list_grid, get_data

data = get_data()
data = data_to_list_grid(data)

##########################################################################

DIRS = [
    ("^", (0, -1)),
    (">", (1, 0)),
    ("v", (0, 1)),
    ("<", (-1, 0)),
]


def find_start(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] in "<>^v":
                return x, y
    raise Exception("Start not found")


def get_patrol_route(x, y, data):
    visited = set()
    d = data[y][x]
    start = (x, y, d)
    for i, d_i in enumerate(DIRS):
        if d_i[0] == d:
            dx, dy = d_i[1]
            di = i

    while True:
        visited.add((x, y))
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= len(data[0]) or ny >= len(data):
            break
        elif data[ny][nx] == "#":
            di = (di + 1) % 4
            d = DIRS[di][0]
            dx, dy = DIRS[di][1]
        else:
            x = nx
            y = ny
            if (x, y, d) == start:
                break
    return visited


def obstructs(x, y, d, data, visited_old):
    for i, d_i in enumerate(DIRS):
        if d_i[0] == d:
            dx, dy = d_i[1]
            di = i
    visited = set([v for v in visited_old])
    while True:
        visited.add((x, y, d))
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= len(data[0]) or ny >= len(data):
            break
        if data[ny][nx] == "#":
            di = (di + 1) % 4
            d = DIRS[di][0]
            dx, dy = DIRS[di][1]
        else:
            x = nx
            y = ny
            if (x, y, d) in visited:
                return True
    return False


def get_patrol_route_2(x, y, data):
    visited = set()
    visited_squares = set()
    d = data[y][x]
    start = (x, y, d)
    for i, d_i in enumerate(DIRS):
        if d_i[0] == d:
            dx, dy = d_i[1]
            di = i
    obstructions = set()
    while True:
        visited.add((x, y, d))
        visited_squares.add((x, y))
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= len(data[0]) or ny >= len(data):
            break
        if data[ny][nx] == "#":
            di = (di + 1) % 4
            d = DIRS[di][0]
            dx, dy = DIRS[di][1]
        else:
            if (
                not (nx == start[0] and ny == start[1])
                and (nx, ny) not in visited_squares
            ):
                nd, (ndx, ndy) = DIRS[(di + 1) % 4]
                obstructed = [[d_ for d_ in d] for d in data]
                obstructed[ny][nx] = "#"
                if obstructs(x, y, nd, obstructed, visited):
                    obstructions.add((nx, ny))
            x = nx
            y = ny
            if (x, y, d) == start:
                break
    return obstructions


def solve_part_1(data):
    x, y = find_start(data)
    visited_squares = get_patrol_route(x, y, data)
    return len(visited_squares)


def solve_part_2(data):
    x, y = find_start(data)
    obstructions = get_patrol_route_2(x, y, data)
    return len(obstructions)


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
