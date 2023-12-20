import copy
import re
from functools import cmp_to_key


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


##########################################################################


def parse_data(data):
    matcher = re.compile("^(\\w) (\\d+) \\(\\#(\\w+)\\)$")
    parsed = list()
    for d in data:
        res = matcher.match(d)
        parsed.append(
            [
                res.groups()[0],
                int(res.groups()[1]),
                res.groups()[2],
            ]
        )

    return parsed


def get_lines(instructions):
    x = 0
    y = 0

    dl = {
        "L": [-1, 0],
        "R": [1, 0],
        "U": [0, -1],
        "D": [0, 1],
    }
    lines = list()
    for instruction in instructions:
        dx, dy = dl[instruction[0]]
        x_n = x + dx * instruction[1]
        y_n = y + dy * instruction[1]
        lines.append([[x, y], [x_n, y_n], instruction[2]])
        y = y_n
        x = x_n
    return lines


def get_vertical_lines(lines):
    vertical_lines = list()
    min_y = max_y = None
    horizontal_lines = dict()
    for l in lines:
        if l[0][0] == l[1][0]:
            if l[0][1] < l[1][1]:
                vertical_lines.append(l)
            else:
                vertical_lines.append([l[1], l[0], l[2]])

            if min_y is None or vertical_lines[-1][0][1] < min_y:
                min_y = vertical_lines[-1][0][1]
            if max_y is None or vertical_lines[-1][1][1] > max_y:
                max_y = vertical_lines[-1][1][1]
        else:
            if l[0][0] < l[1][0]:
                horizontal_lines[tuple(l[0])] = tuple(l[1])
            else:
                horizontal_lines[(l[1][0], l[1][1])] = tuple(l[0])

    return vertical_lines, min_y, max_y, horizontal_lines


def vertical_line_sorter(line_1, line_2):
    if line_1 == line_2:
        return 0
    if line_1[0][0] < line_2[0][0]:
        return -1
    elif line_1[0][0] > line_2[0][0]:
        return 1
    elif line_1[0][1] < line_2[0][1]:
        return -1
    elif line_1[0][1] > line_2[0][1]:
        return 1
    else:
        return 0


def horizontal_line_sorter(line_1, line_2):
    if line_1 == line_2:
        return 0
    elif line_1[0][1] < line_2[0][1]:
        return -1
    elif line_1[0][1] > line_2[0][1]:
        return 1
    if line_1[0][0] < line_2[0][0]:
        return -1
    elif line_1[0][0] > line_2[0][0]:
        return 1
    else:
        return 0


def sort_vlines(lines):
    return sorted(lines, key=cmp_to_key(vertical_line_sorter))


def sort_hlines(lines):
    return sorted(lines, key=cmp_to_key(horizontal_line_sorter))


def realign_lines(lines_r):
    lines = copy.deepcopy(lines_r)
    max_x = None
    max_y = None
    min_x = None
    min_y = None
    for l in lines:
        if min_x is None or l[0][0] < min_x:
            min_x = l[0][0]
        if max_x is None or l[1][0] > max_x:
            max_x = l[1][0]
        if min_y is None or l[0][1] < min_y:
            min_y = l[0][1]
        if max_y is None or l[1][1] > max_y:
            max_y = l[1][1]
    lref = lines
    lines = list()
    new_max_x = max_x - min_x
    new_max_y = max_y - min_y
    for l in lref:
        lines.append(
            ((l[0][0] - min_x, l[0][1] - min_y), (l[1][0] - min_x, l[1][1] - min_y))
        )
    grid = [[None for i in range(0, new_max_x + 1)] for j in range(0, new_max_y + 1)]
    return lines, grid


def draw_grid(lines):
    lines, grid = realign_lines(lines)

    for l in lines:
        for x in range(l[0][0], l[1][0] + 1):
            for y in range(l[0][1], l[1][1] + 1):
                grid[y][x] = "#"

    print(
        "\n".join(
            [
                f"{i:<3} "
                + " ".join([str(g_i) if g_i is not None else " " for g_i in g])
                for i, g in enumerate(grid)
            ]
        )
    )


def split_lines(lines):
    vertical_lines = list()
    min_y = max_y = None
    horizontal_lines = list()
    for l in lines:
        if l[0][0] == l[1][0]:
            if l[0][1] < l[1][1]:
                vertical_lines.append((l[0], l[1]))
            else:
                vertical_lines.append((l[1], l[0]))

            if min_y is None or vertical_lines[-1][0][1] < min_y:
                min_y = vertical_lines[-1][0][1]
            if max_y is None or vertical_lines[-1][1][1] > max_y:
                max_y = vertical_lines[-1][1][1]
        else:
            if l[0][0] < l[1][0]:
                horizontal_lines.append((tuple(l[0]), tuple(l[1])))
            else:
                horizontal_lines.append((tuple(l[1]), tuple(l[0])))
    return sort_vlines(vertical_lines), sort_hlines(horizontal_lines), min_y, max_y


def part_1(data):
    total = 0
    parsed_data = parse_data(data)
    lines = get_lines(parsed_data)
    lines, grid = realign_lines(lines)

    vlines, hlines, min_y, max_y = split_lines(lines)

    mapped_h = {h[0]: h[1] for h in hlines}
    total = [0 for i in range(min_y, max_y + 1)]
    draw_grid(hlines + vlines)
    for i in range(min_y, max_y + 1):
        last_line = None
        last_hline = None
        for j in range(0, len(vlines)):
            start = tuple(vlines[j][0])
            end = tuple(vlines[j][1])
            if i in [10]:
                print(
                    i,
                    start,
                    end,
                    vlines[last_line] if (last_line is not None) else (),
                    last_hline,
                )
            if i >= start[1] and i <= end[1]:
                if last_hline is not None and (
                    start != last_hline and end != last_hline
                ):
                    continue
                if last_line is None:
                    last_line = j
                    if i == start[1] and start in mapped_h:
                        last_hline = mapped_h[start]
                    elif i == end[1] and end in mapped_h:
                        last_hline = mapped_h[end]
                else:
                    if i == 10:
                        print(f"Here on {start} {end}")

                    last_hline = None
                    should_add = True
                    x = start[0]
                    y = start[1]
                    above_count = 0
                    if (x, i) in mapped_h:
                        print(f"Making it false because of mapping")
                        should_add = False
                    else:
                        for h_n, h_l in enumerate(hlines):
                            if x >= h_l[0][0] and x <= h_l[1][0] and h_l[0][1] < y:
                                above_count += 1
                        if i == start[1] and above_count % 2 == 1:
                            should_add = False
                            print(f"Making it false because of hlines odd")

                        elif i == end[1] and above_count % 2 == 0:
                            should_add = False
                            print(f"Making it false because of hlines even")
                    if should_add:
                        to_add = vlines[j][0][0] - vlines[last_line][0][0] + 1
                        if i in [10]:
                            print(
                                f"Adding a line of {to_add} on row {i} between {vlines[last_line]} and {vlines[j]}."
                            )
                        last_line = None
                        last_hline = None
                        total[i] += to_add

    print(f"Part 1: {sum(total)}")
    return total


def part_2(data):
    total = 0

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    data = get_data("data.dat")

    part_1(data)
    part_2(data)
