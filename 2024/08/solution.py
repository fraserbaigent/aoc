import copy


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data):
    coords_map = {}
    for i, d in enumerate(data):
        for j, d_i in enumerate(d):
            if d_i == ".":
                continue
            if d_i not in coords_map:
                coords_map[d_i] = []
            coords_map[d_i].append((j, i))
    return coords_map


def in_bounds(x, y, data):
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data[0]):
        return False
    return True


def solve_part_1(data):
    mapping = parse_data(data)
    antinodes = set()
    for m, v in mapping.items():
        for i in range(0, len(v) - 1):
            for j in range(i + 1, len(v)):
                x0, y0 = v[i]
                x1, y1 = v[j]
                dx = x1 - x0
                dy = y1 - y0

                xx0 = x0 - dx
                yy0 = y0 - dy

                if in_bounds(xx0, yy0, data):
                    antinodes.add((xx0, yy0))

                xx0 = x1 + dx
                yy0 = y1 + dy

                if in_bounds(xx0, yy0, data):
                    antinodes.add((xx0, yy0))

    return len(antinodes)


def print_grid(data, antinodes):
    for i, d in enumerate(data):
        vals = []
        for j, d_i in enumerate(d):
            if d_i == "." and (j, i) in antinodes:
                vals.append("#")
            else:
                vals.append(d_i)
        print("".join(vals))


def solve_part_2(data):
    mapping = parse_data(data)
    antinodes = set()
    for m, v in mapping.items():
        for i in range(0, len(v) - 1):
            for j in range(i + 1, len(v)):

                x0, y0 = v[i]
                x1, y1 = v[j]

                antinodes.add((x0, y0))
                antinodes.add((x1, y1))

                dx = x1 - x0
                dy = y1 - y0

                xx0 = x0 - dx
                yy0 = y0 - dy

                while in_bounds(xx0, yy0, data):
                    antinodes.add((xx0, yy0))
                    xx0 -= dx
                    yy0 -= dy

                xx0 = x1 + dx
                yy0 = y1 + dy

                while in_bounds(xx0, yy0, data):
                    antinodes.add((xx0, yy0))
                    xx0 += dx
                    yy0 += dy

    return len(antinodes)


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
