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


def recurse(line, char_index, current_broken_len, current_broken_index, broken_order, dp_map):
    key = (char_index, current_broken_len, current_broken_index)
    if key in dp_map:
        return dp_map[key]
    
    if char_index == len(line):
        if (
            current_broken_len == 0
            and current_broken_index == len(broken_order)
            ) or (
                current_broken_index == len(broken_order) - 1 and                 
                current_broken_len == broken_order[current_broken_index]
                
            ):
            return 1
        else:
            return 0

    total = 0
    for c in ['#','.']:
        if line[char_index] in [c,'?']:
            if c == '#':
                total += recurse(
                    line,
                    char_index + 1,
                    current_broken_len + 1,
                    current_broken_index,
                    broken_order,
                    dp_map
                    )
            elif c == ".":
                if current_broken_len == 0:
                    total += recurse(
                        line,
                        char_index + 1,
                        0,
                        current_broken_index,
                        broken_order,
                        dp_map,
                        )
                elif (current_broken_index < len(broken_order) and
                      current_broken_len == broken_order[current_broken_index]):
                    total += recurse(
                        line,
                        char_index + 1,
                        0,
                        current_broken_index + 1,
                        broken_order,
                        dp_map
                        )
    dp_map[key] = total
    return total


def get_arrangements_for(line, order):
    dp_map = dict()
    try:
        arrangements = recurse(line, 0, 0, 0, order, dp_map)
    except Exception as e:
        print(line)
        raise e

    return arrangements


def update_for_part_two(data):
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
