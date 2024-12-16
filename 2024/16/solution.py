import copy

from AocCommon import data_to_list_grid, get_data

data = get_data()
data = data_to_list_grid(data)

##########################################################################


def get_points(data):
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)

    return start, end


DIRS = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}

backwards = {"^": "v", ">": "<", "<": ">", "v": "^"}


def solve(data):
    score = [[{d: None for d in DIRS} for n in d] for d in data]
    paths = [[{d: [] for d in DIRS} for n in d] for d in data]
    start, end = get_points(data)
    queue = []
    for d in DIRS:
        x, y = start
        score[y][x][d] = 0
        dy, dx = DIRS[d]
        if data[y + dy][x + dx] == "#":
            continue
        queue.append((d, (x + dx, y + dy), start, d == ">", 0, d))
    while len(queue):
        direction, point, from_point, is_straight, old_score, old_direction = queue.pop(
            0
        )
        x, y = point

        x_o, y_o = from_point

        new_score = old_score + (1 if is_straight else 1001)
        if score[y][x][direction] is not None and score[y][x][direction] < new_score:
            continue
        elif score[y][x][direction] is not None and score[y][x][direction] == new_score:
            paths[y][x][direction].add((from_point, old_direction))
        else:
            score[y][x][direction] = new_score
            paths[y][x][direction] = {(from_point, old_direction)}

        if data[y][x] in "E":
            continue

        for d in DIRS:
            if backwards[direction] == d:
                continue
            dy, dx = DIRS[d]
            if data[y + dy][x + dx] in "#":
                continue

            queue.append(
                (
                    d,
                    (x + dx, y + dy),
                    (x, y),
                    (from_point is None or d == direction),
                    score[y][x][direction],
                    direction,
                )
            )
    return score, paths, end


def solve_part_1(data):
    score, paths, end = solve(data)
    return min([v for v in score[end[1]][end[0]].values() if v is not None])


def solve_part_2(data):
    score, paths, end = solve(data)

    end_d = None
    end_score = None
    for d, v in score[end[1]][end[0]].items():
        if v is None:
            continue
        if end_d is None or end_score is None or v < score[end[1]][end[0]][end_d]:
            end_d = d
            end_score = v
    pts = {end}
    added = set()
    to_add = [p for p in paths[end[1]][end[0]][end_d]]
    while len(to_add):
        pt, d = to_add.pop(0)
        pts.add(pt)
        x, y = pt
        for p in paths[y][x][d]:
            if p in added:
                continue
            to_add.append(p)
            added.add(p)
    for x, y in pts:
        data[y][x] = "O"

    #    print("\n".join(["".join(d) for d in data]))
    return len(pts)


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
