import json
import re
import copy

def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_input(data):
    rx = re.compile("^(\\w+)\\: (.*)$")
    parsed = dict()
    for d in data:
        re_m = rx.match(d)
        res = re_m.groups()[0]
        others = re_m.groups()[1].split(" ")
        for o in others:
            o = o.strip()
            if res not in parsed:
                parsed[res] = set()
            parsed[res].add(o)
            if o not in parsed:
                parsed[o] = set()
            parsed[o].add(res)
    return parsed

def get_group(element, parsed_input, seen):
    seen.add(element)
    group = {element}
    for el in parsed_input[element]:
        if el in seen:
            continue
        g = get_group(el, parsed_input, seen)
        for g_ in g:
            group.add(g_)
    return group
        
        

def get_groups(parsed_input):
    seen = set()
    groups = []
    for p in parsed_input:
        if p in seen:
            continue
        group = get_group(p, parsed_input, seen)
        groups.append(group)

    return groups
def part_1(data):
    total = 0
    parsed_input = parse_input(data)
    print(len(parsed_input))
    groups = get_groups(parsed_input)
#    print(groups)
    print(f"Part 1: {total}")
    return 1


def part_2(data):
    total = 0

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
