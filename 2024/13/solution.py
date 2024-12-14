import re

from AocCommon import get_data


def parse_data(data : list, part_2 : bool):
    parsed = list()
    i = 0
    while i < len(data):
        if len(data[i].strip()) == 0:
            i += 1
            continue
        dx_a, dy_a = tuple(
            [int(d) for d in data[i].replace(",", "").replace("Y", "").split("+")[1:]]
        )
        dx_b, dy_b = tuple(
            [
                int(d)
                for d in data[i + 1].replace(",", "").replace("Y", "").split("+")[1:]
            ]
        )
        x, y = tuple(
            [
                float(d) + (10000000000000 if part_2 == True else 0)
                for d in data[i + 2].replace(",", "").replace("Y", "").split("=")[1:]
            ]
        )

        i += 3
        parsed.append(
            {"x": x, "y": y, "dx_a": dx_a, "dy_a": dy_a, "dx_b": dx_b, "dy_b": dy_b}
        )
    return parsed


data = get_data()

##########################################################################

# a = x / dx_a - (b * dx_b / dx_a)
# b = y / dy_b - (a * dy_a / dy_b)
# a = x / dx_a - (dx_b / dx_a) * (y / dy_b - a * (dy_a / dy_b)
# a = (x /dx_a - (dx_b / dx_a) * (y / dy_b) ) / (1 - (dx_b / dx_a)* (dy_a/
# dy_b))


def get_a(x, dx_a, y, dy_a, dx_b, dy_b):
    a = (x / dx_a - (dx_b / dx_a) * (y / dy_b)) / (1. - (dx_b / dx_a) * (dy_a / dy_b))
    return a


def test_x(a, b, dx_a, dx_b, **kwargs):
    return dx_a * a + dx_b * b


def test_y(a, b, dy_a, dy_b, **kwargs):
    return dy_a * a + dy_b * b


def get_b(x, dx_a, y, dy_a, dx_b, dy_b, a):
    b = (y / dy_b) - (a * dy_a / dy_b)
    return b

def solve(data, is_part_2):
    parsed = parse_data(data, is_part_2)
    tokens = 0
    for p in parsed:
        a = get_a(**p)
        err = a - float(round(a))
        if (a > 100.0 and not is_part_2) or abs(err) > 0.001:
            continue
        a = round(a)
        b = get_b(**p, a=a)
        err = b - float(round(b))
        if (b > 100.0 and not is_part_2) or abs(err) > 0.001:
            continue
        b = round(b)
        x = test_x(a, b, **p)
        y = test_y(a, b, **p)
        tokens += 3 * a + b
    return tokens

def part_1(data):
    total = solve(data, False)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = solve(data, True)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
