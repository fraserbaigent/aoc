from AocCommon import get_data, split_data_with_regex

##########################################################################

X_LIM = 101
Y_LIM = 103


def quadrant(x, y, x_lim, y_lim):
    if x == (x_lim // 2) or y == (y_lim // 2):
        return None
    if x < (x_lim // 2):
        if y <= (y_lim // 2):
            return 0
        else:
            return 1
    else:
        if y < (y_lim // 2):
            return 2
        else:
            return 3


def translate(data, time_steps, x_lim, y_lim):
    end_positions = list()
    for d in data:
        x, y, v_x, v_y = tuple(d)
        x_end = (x + v_x * time_steps) % x_lim
        y_end = (y + v_y * time_steps) % y_lim
        end_positions.append((x_end, y_end))
    return end_positions


def print_data(key, step, cache):
    if key not in cache:
        cache[key] = step
        return False
    return True
    #    print(f"Step {step} - first seen at {cache[key]} ({step - cache[key]})")
    # for y in range(0, Y_LIM):
    #    to_print = []
    #    for x in range(0, X_LIM):
    #        if (x, y) in key:
    #            to_print.append("#")
    #        else:
    #            to_print.append(".")
    #    print("".join(to_print))
    # return True


def solve_part_1(data, time_steps, x_lim=X_LIM, y_lim=Y_LIM):
    end_positions = translate(data, time_steps, x_lim, y_lim)

    quadrants = {i: 0 for i in range(0, 4)}
    for x, y in end_positions:
        res = quadrant(x, y, x_lim, y_lim)
        if res is not None:
            quadrants[res] += 1
    total = 1
    for _, v in quadrants.items():
        total *= v
    return total


def get_key(data):
    vals = set([(d[0], d[1]) for d in data])
    return tuple(sorted([v for v in vals]))


def is_neighbour(pt1, pt2):
    if pt1 == pt2:
        return True
    for dx in [-1, 0, +1]:
        for dy in [-1, 0, +1]:
            if pt1[0] + dx == pt2[0] and pt1[1] + dy == pt2[1]:
                return True
    return False


def get_score(key):
    # number of points that have neighbours - heuristically the tree should
    # have lots of points next to each other, let's see...
    has_neighbours = {k: False for k in key}
    for k in key:
        if has_neighbours[k] == True:
            continue
        for k2 in key:
            if k == k2 or has_neighbours[k2]:
                continue
            if is_neighbour(k, k2):
                has_neighbours[k] = True
                has_neighbours[k2] = True
                break
    return sum([1 for k, v in has_neighbours.items() if v == True])


def solve_part_2(data, x_lim, y_lim):
    now_data = [list(d) for d in data]
    step = 0
    cache = dict()
    scores = dict()
    while True:
        #        print(f"Solving step {step:>5}", end="\r", flush=True)
        key = get_key(now_data)
        scores[key] = get_score(key)
        if print_data(key, step, cache) == True:
            break
        for i, n in enumerate(now_data):
            n[0] = (n[0] + n[2]) % x_lim
            n[1] = (n[1] + n[3]) % y_lim
            data[i] = n
        step += 1
    s = sorted(
        list(scores.keys()),
        key=lambda k: float(scores[k]) / float(len(k)),
        reverse=True,
    )
    return cache[s[0]]


def part_1(data):
    total = solve_part_1(data, 100)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = solve_part_2(data, X_LIM, Y_LIM)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    data = get_data()
    data = split_data_with_regex(
        data, "p=(.*),(.*) v=(.*),(.*)", types=[int, int, int, int]
    )
    part_1(data)
    part_2(data)
