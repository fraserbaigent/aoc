import json


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def get_start_end(data):
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "E":
                end = (x, y)
            elif c == "S":
                start = (x, y)
    return start, end


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_bounds(x_, y_):
    return x_ >= 0 and y_ >= 0 and y_ < len(data) and x_ < len(data[0])


def get_common(data):
    start, end = get_start_end(data)
    to_end = dict()

    checks = [(end, 0)]

    while len(checks):
        (x, y), s = checks.pop(0)
        to_end[(x, y)] = s
        for dx, dy in DIRS:
            xx = x + dx
            yy = y + dy
            if not in_bounds(xx, yy) or data[yy][xx] == "#" or (xx, yy) in to_end:
                continue

            checks.append(((xx, yy), s + 1))
    return start, end, to_end


def solve_part_1(data):
    start, end, to_end = get_common(data)
    scores = {}
    savings = {}
    for x, y in to_end:
        to_check = list()
        for dx, dy in DIRS:
            xx = x + dx
            yy = y + dy
            if not in_bounds(xx, yy) or data[yy][xx] != "#":
                continue

            for dxx, dyy in DIRS:
                xxx = xx + dxx
                yyy = yy + dyy
                if (
                    not in_bounds(xxx, yyy)
                    or (xxx, yyy) == (x, y)
                    or data[yyy][xxx] == "#"
                ):
                    continue
                to_check.append((xxx, yyy))
        for t in to_check:
            other = to_end[t]
            saving = to_end[(x, y)] - (other + 2)

            if saving > 0:
                if saving not in scores:
                    scores[saving] = 0
                scores[saving] += 1
    return scores


def cheat(start, lookup, limit):
    seen = set()
    to_go = [(start, 0)]
    savings = dict()
    while len(to_go):
        (x, y), t = to_go.pop(0)
        if (x, y) in seen:
            continue
        if t > limit or (x, y) in savings:
            continue

        seen.add((x, y))
        if t > 0 and (x, y) in lookup:
            saving = lookup[start] - (lookup[(x, y)] + t)
            savings[(x, y)] = saving
            continue
        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy
            if not in_bounds(nx, ny):
                continue
            to_go.append(((nx, ny), t + 1))
    return savings.values()


def solve_part_2(data, minimum=0):
    start, end, to_end = get_common(data)
    scores = dict()
    for start in to_end:
        score = cheat(start, to_end, 20)
        for s in score:
            if s not in scores:
                scores[s] = 0
            scores[s] += 1
    return {k: v for k, v in scores.items() if k >= minimum}


def part_1(data):
    scores = solve_part_1(data)
    for s in sorted(scores, reverse=True):
        if s >= 100:
            print(s, scores[s])
    total = sum([v for s, v in scores.items() if s >= 100])
    print(f"Part 1: {total}")
    return total


def part_2(data):
    scores = solve_part_2(data)
    total = sum([v for s, v in scores.items() if s >= 100])
    print(f"Part 1: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
