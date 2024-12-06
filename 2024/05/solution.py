def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_inputs(data):
    mappings = dict()
    commands = list()
    for d in data:
        if len(d) == 0:
            continue
        if "|" in d:
            v = [int(a) for a in d.split("|")]
            if v[0] not in mappings:
                mappings[v[0]] = set()
            mappings[v[0]].add(v[1])
        else:
            commands.append([int(a) for a in d.split(",")])
    return mappings, commands


def get_good_lines(mappings, commands):
    good_lines = list()
    for c in commands:
        good = True
        for i in range(0, len(c) - 1):
            for j in range(i + 1, len(c)):
                if not (
                    c[j] in mappings.get(c[i], []) or c[i] not in mappings.get(c[j], [])
                ):
                    good = False

        if good == True:
            good_lines.append(c)
    return good_lines


def solve_part_1(data):
    mappings, commands = parse_inputs(data)
    good_lines = get_good_lines(mappings, commands)

    total = 0
    for g in good_lines:
        total += g[len(g) // 2]
    return total


def correct(mappings, bad_lines):
    for b in bad_lines:
        i = 0
        while i < len(b) - 1:
            j = i + 1
            swapped = False
            while j < len(b):
                left = b[i]
                right = b[j]
                left_mapping = mappings.get(left, [])
                right_mapping = mappings.get(right, [])
                if right in left_mapping or left not in right_mapping:
                    j += 1
                    continue
                b[i] = right
                b[j] = left
                swapped = True
                break
            if swapped == False:
                i += 1
    return bad_lines


def solve_part_2(data):
    mappings, commands = parse_inputs(data)
    good_lines = get_good_lines(mappings, commands)
    bad_lines = [c for c in commands if c not in good_lines]

    corrected_bad_lines = correct(mappings, bad_lines)
    total = 0
    for g in bad_lines:
        total += g[len(g) // 2]
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
