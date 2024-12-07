import re

from AocCommon import get_data

data = get_data()

##########################################################################


def parse_data(data):
    parsed = []
    regex = re.compile("(\\d+): (.*)")
    for d in data:
        res = regex.match(d)
        parsed.append((int(res.groups()[0]), [int(i) for i in res.groups()[1].split()]))

    return parsed


def recurse(total, values, operator, operators):
    if operator == operators[0]:
        val = sum(values[:2])
    elif operator == operators[1]:
        val = values[0] * values[1]
    elif len(operators) > 2 and operator == operators[2]:
        val = int(f"{values[0]}{values[1]}")

    if len(values) == 2:
        return val == total
    else:
        new_values = [val]
        for v in values[2:]:
            new_values.append(v)
        for o in operators:
            if recurse(total, new_values, o, operators):
                return True
        return False


def is_true(total, values, operators):
    for o in operators:
        if recurse(total, values, o, operators):
            return True
    return False


def solve_part_1(data):
    parsed_data = parse_data(data)
    total = 0
    for t, v in parsed_data:
        if is_true(t, v, ["+", "*"]):
            total += t
    return total


def solve_part_2(data):
    parsed_data = parse_data(data)
    total = 0
    for t, v in parsed_data:
        if is_true(t, v, ["+", "*", "||"]):
            total += t
    return total


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
