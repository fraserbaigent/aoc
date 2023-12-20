import copy
import json
import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data):
    rx = re.compile("^(\\w+)\\{(.*)\\}$")
    sm = re.compile("^\\{x=(\\d+),m=(\\d+),a=(\\d+),s=(\\d+)\\}$")
    rm = re.compile("^([amxs]{1})([\\>\\<])(\\d+)\\:(\\w+)$")
    rules = dict()
    instructions = list()
    for d in data:
        if len(d.strip()) == 0:
            continue
        elif res := rx.match(d):
            v = res.groups()[1].split(",")
            my_rules = list()
            for v_i in v:
                if res_2 := rm.match(v_i):
                    my_rules.append(
                        {
                            "key": res_2.groups()[0],
                            "op": res_2.groups()[1],
                            "val": int(res_2.groups()[2]),
                            "res": res_2.groups()[3],
                        }
                    )
                else:
                    my_rules.append({"res": v_i})
            rules[res.groups()[0]] = my_rules

        else:
            res = sm.match(d)

            instructions.append(
                {
                    "x": int(res.groups()[0]),
                    "m": int(res.groups()[1]),
                    "a": int(res.groups()[2]),
                    "s": int(res.groups()[3]),
                }
            )
    return rules, instructions


def process_for(rule_key, rules, val, visited_rules):
    if rule_key in visited_rules:
        return visited_rules[rule_key]

    rule = rules[rule_key]
    for r_i in rule:
        if "key" in r_i:
            if r_i["op"] == ">":
                if val[r_i["key"]] > r_i["val"]:
                    instruction = r_i["res"]
                else:
                    continue
            else:
                if val[r_i["key"]] < r_i["val"]:
                    instruction = r_i["res"]
                else:
                    continue
        else:
            instruction = r_i["res"]
        if instruction == "R":
            visited_rules[rule_key] = "R"
            return "R"
        elif instruction == "A":
            visited_rules[rule_key] = "A"
            return "A"
        else:
            res = process_for(r_i["res"], rules, val, visited_rules)
            return res


def get_accepted(rules, instructions):
    accepted = list()

    for i in instructions:
        visited_rules = dict()
        result = process_for("in", rules, i, visited_rules)
        if result == "A":
            accepted.append(sum(i.values()))

    return accepted


def try_solve(rules):
    rule_results = {}
    instructions = []
    instructions.append(["in", {"a": None, "s": None, "m": None, "x": None}])
    while len(instructions) > 0:
        v = instructions.pop(0)
        rule = rules[v[0]]
        i = copy.deepcopy(v[1])

        bad = None
        for r_i in rule:
            if "key" in r_i:

                good = r_i["val"]
                good += 1 if r_i["op"] == ">" else -1

            else:
                instruction = r_i["res"]

            if r_i["op"] == ">":
                if val[r_i["key"]] > r_i["val"]:
                    instruction = r_i["res"]
                else:
                    continue
            else:
                if val[r_i["key"]] < r_i["val"]:
                    instruction = r_i["res"]
                else:
                    continue
        else:
            instruction = r_i["res"]
        if instruction == "R":
            return None
        elif instruction == "A":
            visited_rules[rule_key] = "A"
            return values
        else:
            return process_for(instruction, rules, values, rule_results)


def solve_part_2(rules):
    rules, _ = parse_data(data)
    values = part_2_sol(rules)
    return values


def part_1(data):
    total = 0
    rules, instructions = parse_data(data)
    accepted = get_accepted(rules, instructions)
    total = sum(accepted)
    print(f"Part 1: {total}")
    return total


def calculate_total(ranges):
    total = 1
    for k, v in ranges.items():
        total *= max(v[1] - v[0] + 1, 0)
    return total


class Range:

    def __init__(self, letter, lower, upper, child_ranges):
        self.letter = letter
        self.lower = lower
        self.upper = upper
        self.child_ranges = child_ranges


def part_2_sol(rules):
    total = 0
    next_items = list()
    next_items.append(("in", {i: [1, 4000] for i in "xmas"}))
    accepted = list()
    while len(next_items) > 0:
        item = next_items.pop(0)
        if item[0] == "R":
            continue
        elif item[0] == "A":
            accepted.append(item[1])
            continue
        rule = rules[item[0]]
        for r_i in rule:
            map_copy = copy.deepcopy(item[1])
            if "op" in r_i:
                if r_i["op"] == ">":
                    map_copy[r_i["key"]][0] = max(
                        map_copy[r_i["key"]][0], r_i["val"] + 1
                    )
                elif r_i["op"] == "<":
                    map_copy[r_i["key"]][1] = min(
                        map_copy[r_i["key"]][1], r_i["val"] - 1
                    )
                else:
                    raise Exception("Wrong operator!")
                if map_copy[r_i["key"]][0] > map_copy[r_i["key"]][1]:
                    continue
                next_items.append((r_i["res"], map_copy))
            else:
                next_items.append((r_i["res"], copy.deepcopy(item[1])))

    x_list = []
    for a in accepted:
        next_update = x_list
        for x, r in a.items():
            x_min, x_max = tuple(r)
            updated_ranges = update_ranges(next_update, x_min, x_max)
            next_update = []
            for n in updated_ranges:
                next_update += n.child_ranges

    return total


def update_ranges(
    range_list,
    x_min,
    x_max,
):
    if len(range_list) == 0:
        range_list.append(Range(x_min, x_max, []))
        return range_list

    updated_ranges = list()
    left = None
    for r in range_list:
        if x_min == r.lower and x_max == r.upper:
            updated_ranges.append(r)
            return updated_ranges
        elif r.upper < x_min:
            continue
        if r.lower < min_x and r.upper > max_x:
            mid_copy = copy.deepcopy(r)
            top_copy = copy.deepcopy(r)
            r.upper = min_x - 1
            mid_copy.lower = min_x
            mid_copy.upper = max_x
            top_copy.lower = max_x + 1
            range_list.append(r)
            range_list.append(mid_copy)
            range_list.append(top_copy)
            return [r, mid_copy, top_copy]
        if r.lower > x_min and r.upper < x_max:
            bottom_copy = copy.deepcopy(r)
            upper_copy = copy.deepcopy(r)
            bottom_copy.lower = min_x
            bottom_copy.upper = r.lower - 1
            top_copy.lower = r.upper + 1
            top_copy.upper = max_x
            range_list.append(r)
            range_list.append(mid_copy)
            range_list.append(top_copy)
            return [r, mid_copy, top_copy]

    return updated_ranges


def part_2(data):
    total = 0
    rules, _ = parse_data(data)
    total = solve_part_2(rules)
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
