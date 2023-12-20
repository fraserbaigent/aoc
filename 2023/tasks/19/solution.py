import json
import re
import copy

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
    instructions.append(['in', {'a':None,'s':None,'m':None,'x':None}])
    while len(instructions) > 0:
        v = instructions.pop(0)
        rule = rules[v[0]]
        i = copy.deepcopy(v[1])

        bad = None
        for r_i in rule:
            if "key" in r_i:
                
                good = r_i['val']
                good += 1 if r_i['op'] == '>' else -1
                
            else:
                instruction = r_i['res']

                
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
    #    start = rules['in']
    rule_results = dict()
    values = try_solve("in", rules, values)
    return values
    
def part_1(data):
    total = 0
    rules, instructions = parse_data(data)
    accepted = get_accepted(rules, instructions)
    total = sum(accepted)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    rules, _ = parse_data(data)
    total = solve_part_2(rules)
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
