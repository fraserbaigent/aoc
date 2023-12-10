import math
import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_input(data):
    i_re = re.compile("^(\\w{3}) = \\((\\w{3})\\, (\\w{3})\\)$")

    parsed = dict()
    for l in data:
        if len(l) == 0:
            continue
        m = i_re.match(l)
        if m is None:
            instructions = l
            continue
        parsed[m.groups()[0]] = [m.groups()[1], m.groups()[2]]
    return instructions, parsed


def get_initial_next_steps(parsed_input):
    return set([i for i in parsed_input.keys() if i[2] == "A"])


def get_to_end(instructions, parsed_input, steps):
    steps_taken = set()
    for s in steps:
        i = 0
        step = s
        while step[2] != "Z":
            instruction = instructions[i % len(instructions)]
            i += 1
            d = 0 if instruction == "L" else 1
            step = parsed_input[step][d]
        steps_taken.add(i)
    return math.lcm(*list(steps_taken))


def part_1(data):
    total = 0
    instructions, parsed = parse_input(data)

    total = get_to_end(instructions, parsed, ["AAA"])

    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    instructions, parsed = parse_input(data)
    steps = get_initial_next_steps(parsed)
    total = get_to_end(instructions, parsed, steps)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
