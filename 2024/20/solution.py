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


def solve_part_1(data):
    start, end = get_start_end(data)
    to_end = dict()

    checks = [(end, 0)]

    def in_bounds(x_, y_):
        return x_ >= 0 and y_ >= 0 and y_ < len(data) and x_ < len(data[0])

    while len(checks):
        (x, y), s = checks.pop(0)
        to_end[(x, y)] = s
        for dx, dy in DIRS:
            xx = x + dx
            yy = y + dy
            if not in_bounds(xx, yy) or data[yy][xx] == "#" or (xx, yy) in to_end:
                continue

            checks.append(((xx, yy), s + 1))

    scores = {}
    for x, y in to_end:
        to_check = list()
        for dx, dy in DIRS:
            xx = x + dx
            yy = y + dx
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
            saving = to_end[(x, y)] - (other)
            if saving > 0:
                if saving not in scores:
                    scores[saving] = 0
                scores[saving] += 1
    for k in sorted(list(scores.keys())):  # , key=lambda k: scores[k]):
        print(k, scores[k])

    #    print(json.dumps(scores, indent=4))
    return sum([1 for s, v in scores.items() if v >= 100])


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
