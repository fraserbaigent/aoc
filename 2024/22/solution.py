import math

from AocCommon import submit


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def mix(one, two):
    return one ^ two


def prune(number):
    return number % 16777216


def generate_secret(original):
    updated = mix(original, original * 64)
    updated = prune(updated)

    updated = mix(updated, int(math.floor(updated / 32.0)))
    updated = prune(updated)

    updated = mix(updated, updated * 2048)
    return prune(updated)


def solve_part_1(data):
    data = [int(d) for d in data]
    total = 0
    for d in data:
        for i in range(0, 2000):
            d = generate_secret(d)
        total += d
    return total


def solve_part_2(data):
    data = [int(d) for d in data]
    sells = []
    print(data)
    for d in data:
        sequence = []
        sell_data = {}
        previous = int(str(d)[-1])
        for i in range(0, 2000):
            d = generate_secret(d)
            price = int(str(d)[-1])

            delta = price - previous
            previous = price
            sequence.append(delta)
            if len(sequence) > 4:
                sequence.pop(0)
            if len(sequence) == 4:
                key = tuple(sequence)
                if key not in sell_data:
                    sell_data[key] = price
        sells.append(sell_data)

    options = set()
    for s in sells:
        options |= set(s.keys())

    total = 0
    max_path = None
    for o in options:
        tot = 0
        for s in sells:
            tot += s.get(o, 0)
        if tot > total:
            max_path = o
        total = max(tot, total)
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
