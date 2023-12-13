import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################
data_re = re.compile("^([\\.\\#\\?]+) (.*)$")


def parse_data(data):
    parsed_data = list()
    for d in data:
        res = data_re.match(d.strip())
        parsed_data.append(
            [res.groups()[0], [int(i.strip()) for i in res.groups()[1].split(",")]]
        )
    return parsed_data


def is_operational(spring):
    return spring == "."


def is_broken(spring):
    return spring == "#"


def is_questionable(spring):
    return spring == "?"


def recurse(line, char_index, current_broken_len, current_broken_index, broken_order):
    if current_broken_index > len(broken_order) or (
        current_broken_index == len(broken_order) and current_broken_len > 0
    ):
        return 0

    if char_index == len(line):
        if (
            current_broken_len > 0
            and current_broken_len == broken_order[current_broken_index]
            and current_broken_index == len(broken_order) - 1
        ) or (current_broken_len == 0 and current_broken_index == len(broken_order)):
            return 1
        else:
            return 0
    if line[char_index] == "#":
        current_broken_len += 1
        return recurse(
            line, char_index + 1, current_broken_len, current_broken_index, broken_order
        )
    if line[char_index] == ".":
        if current_broken_len == 0:
            return recurse(
                line,
                char_index + 1,
                0,
                current_broken_index,
                broken_order,
            )
        elif current_broken_len != broken_order[current_broken_index]:
            return 0
        else:
            return recurse(
                line, char_index + 1, 0, current_broken_index + 1, broken_order
            )
    if line[char_index] == "?":
        total = 0
        if (
            current_broken_index < len(broken_order)
            and current_broken_len < broken_order[current_broken_index]
        ):
            total += recurse(
                line,
                char_index + 1,
                current_broken_len + 1,
                current_broken_index,
                broken_order,
            )
        if current_broken_len == 0:
            total += recurse(
                line,
                char_index + 1,
                0,
                current_broken_index,
                broken_order,
            )
        elif current_broken_len == broken_order[current_broken_index]:
            total += recurse(
                line, char_index + 1, 0, current_broken_index + 1, broken_order
            )
        return total


def get_arrangements_for(line, order):
    try:
        arrangements = recurse(line, 0, 0, 0, order)
    except Exception as e:
        print(line)
        raise e

    return arrangements


def update_for_part_two(data):
    for i, d in enumerate(data):
        new_str = ""
        last_was_dot = False
        for d_i in d[0]:
            if d_i == ".":
                if not last_was_dot:
                    new_str += "."
                    last_was_dot = True
            else:
                new_str += d_i
                last_was_dot = False
        data[i][0] = new_str
    new_line = "?".join([data[0] for i in range(0, 5)])
    new_order = list()
    for i in range(0, 5):
        new_order += data[1]

    return [new_line, new_order]


def part_1(data):
    total = 0
    parsed_data = parse_data(data)
    for p in parsed_data:
        line = p[0]
        order = p[1]
        arrangements = get_arrangements_for(line, order)
        total += arrangements
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    total = 0
    parsed_data = parse_data(data)
    parsed_data = [update_for_part_two(p) for p in parsed_data]
    for p in parsed_data:
        line = p[0]
        order = p[1]
        arrangements = get_arrangements_for(line, order)
        total += arrangements

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
