import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data):
    parsed = {}

    seeds_re = re.compile("seeds: (.*)")
    parsed["seeds"] = [
        int(i.strip()) for i in seeds_re.match(data[0]).groups()[0].strip().split(" ")
    ]
    parsed["maps"] = {}
    current_line_name = None
    range_re = re.compile("^(\\d+) (\\d+) (\\d+)$")
    line_name_re = re.compile("^(\\w+)\\-to\\-(\\w+) map:$")
    for d in data[1:]:
        if len(d.strip()) == 0:
            continue
        if result := range_re.match(d):
            parsed["maps"][current_line_name]["mappings"].append(
                tuple([int(i) for i in result.groups()])
            )
        elif result := line_name_re.match(d):
            current_line_name = result.groups()[0]
            parsed["maps"][current_line_name] = {
                "to": result.groups()[1],
                "mappings": list(),
            }

    for d in parsed["maps"]:
        parsed["maps"][d]["mappings"] = sorted(
            parsed["maps"][d]["mappings"], key=lambda k: k[1]
        )
    return parsed


def find_lowest_seed(seeds, maps):
    lowest_seed = None

    for s in seeds:
        key = "seed"
        mapped_val = s
        while True:
            data = maps[key]["mappings"]
            i = 0
            while i < len(data):
                dat = data[i]
                if mapped_val < dat[1]:
                    break
                elif mapped_val >= dat[1] and mapped_val <= dat[1] + dat[2]:
                    mapped_val = dat[0] + (mapped_val - dat[1])
                    break
                i += 1
            key = maps[key]["to"]
            if key not in maps:
                if lowest_seed is None or mapped_val < lowest_seed:
                    lowest_seed = mapped_val
                break

    return lowest_seed


def find_lowest_seed_2(seeds, maps):
    lowest_seed = None

    key = "seed"
    current_seeds = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
    next_seeds = list()
    while len(current_seeds) > 0:
        mapped_val = maps[key]
        data = mapped_val["mappings"]
        next_item = mapped_val["to"]
        for s in current_seeds:
            i = 0
            start = s[0]
            end = s[0] + s[1] - 1
            while i < len(data):
                d = data[i]
                l = d[1]
                r = d[1] + d[2] - 1
                if end < l:
                    i += 1
                    continue
                elif start > r:
                    i += 1
                    continue
                elif start >= l and end <= r:
                    s_delta = start - l
                    next_seeds.append([d[0] + s_delta, s[1]])
                    break
                elif start < l and (end >= l and end <= r):
                    next_seeds.append([start, l - start])
                    width = end - l + 1
                    next_seeds.append([d[0], width])
                    break
                elif start >= l and start <= r and end > r:
                    s_delta = start - l
                    next_seeds.append([d[0] + s_delta, r - start + 1])
                    start = r + 1
                    i += 1
                elif start < l and end > r:
                    next_seeds.append([start, l - start])
                    next_seeds.append([d[0], d[2]])
                    start = r + 1
                    i += 1
                else:
                    print(d, s, "this")
                    exit()
            if i >= len(data):
                next_seeds.append([start, end - start + 1])
        next_seeds = sorted(next_seeds, key=lambda k: k[0])
        if next_item not in maps:
            current_seeds = []
            for s in next_seeds:
                if lowest_seed is None or s[0] < lowest_seed:
                    lowest_seed = s[0]
            break
        else:
            key = next_item
            current_seeds = next_seeds
            next_seeds = []

    return lowest_seed


def part_1(data):
    parsed_data = parse_data(data)
    total = find_lowest_seed(**parsed_data)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    parsed_data = parse_data(data)
    total = find_lowest_seed_2(**parsed_data)
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
