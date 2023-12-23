import re

import numpy as np


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################

BUTTON = -1
BROADCASTER = 0
FLIP_FLOP = 1
CONJUNCTION = 2
LOW = 0
HIGH = 1


def parse_data(data):
    matcher = re.compile("^(.*) \\-\\> (.*)$")
    rules = {
        "button": {
            "type": BUTTON,
            "vals": ["broadcaster"],
        }
    }
    for d in data:
        res = matcher.match(d).groups()
        ty = res[0][0]
        vals = [v.strip() for v in res[1].split(",")]
        if ty == "%":
            rules[res[0][1:]] = {
                "type": FLIP_FLOP,
                "vals": vals,
            }
        elif ty == "&":
            rules[res[0][1:]] = {
                "type": CONJUNCTION,
                "vals": vals,
            }
        else:
            rules[res[0]] = {
                "type": BROADCASTER,
                "vals": vals,
            }

    cjs = [r for r in rules if rules[r]["type"] == CONJUNCTION]
    for c in cjs:
        rules[c]["inputs"] = []
        for r in rules:
            if c in rules[r]["vals"]:
                rules[c]["inputs"].append(r)
    return rules


def hash_config(configuration):
    hash_string = ""
    for k in sorted(list(configuration.keys())):
        hash_string += f"{k}{configuration[k]};"
    return hash_string


def push_button(configuration, rules):
    low = high = 0
    commands = [("button", None, None)]
    while len(commands) > 0:
        command, input_id, c_type = commands.pop(0)

        if command not in rules:
            rule = {"type": None}
        else:
            rule = rules[command]
        if rule["type"] is None:
            pass
        elif rule["type"] == BUTTON:
            commands.append(("broadcaster", command, LOW))
        elif rule["type"] == BROADCASTER:
            for v in rule["vals"]:
                commands.append((v, command, c_type))
        elif rule["type"] == FLIP_FLOP:
            if c_type is not HIGH:
                if configuration[command] == False:
                    configuration[command] = True
                    to_send = HIGH
                else:
                    configuration[command] = False
                    to_send = LOW
                for v in rule["vals"]:
                    commands.append((v, command, to_send))
        elif rule["type"] == CONJUNCTION:
            configuration[command][input_id] = c_type
            all_are_high = True
            for i_id in configuration[command]:
                if configuration[command][i_id] == LOW:
                    all_are_high = False
                    break
            for v in rule["vals"]:
                commands.append((v, command, LOW if all_are_high else HIGH))

        if c_type is not None:
            if c_type == HIGH:
                high += 1
            elif c_type == LOW:
                low += 1

    return low, high


def get_pulses(rules, pulse_count):
    pulse_cache = dict()
    high = low = 0
    configuration = dict()
    cache = dict()
    results = list()

    for p in rules:
        if rules[p]["type"] == FLIP_FLOP:
            configuration[p] = False
        elif rules[p]["type"] == CONJUNCTION:
            configuration[p] = {k: LOW for k in rules[p]["inputs"]}

    for p in range(0, pulse_count):
        original_configuration = hash_config(configuration)
        if original_configuration in cache:
            interval = p - cache[original_configuration]
            low_int = sum(
                [results[i][LOW] for i in range(cache[original_configuration], p)]
            )
            high_int = sum(
                [results[i][HIGH] for i in range(cache[original_configuration], p)]
            )

            remaining = pulse_count - p
            interval_count = int(np.floor(remaining / interval))
            remainder = remaining % interval
            low += interval_count * low_int
            high += interval_count * high_int
            for i in range(0, remainder):
                low += results[cache[original_configuration] + i][LOW]
                high += results[cache[original_configuration] + i][HIGH]
            break
        low_i, high_i = push_button(configuration, rules)
        low += low_i
        high += high_i
        cache[original_configuration] = p
        results.append((low_i, high_i))

    return high, low

def find_first_highs_at(rules_to_find, rules, conjunction_to_check):
    configuration = dict()
    print(f'Looking for the first occurance of a HIGH at {conjunction_to_check} for inputs {rules_to_find}')
    for p in rules:
        if rules[p]["type"] == FLIP_FLOP:
            configuration[p] = False
        elif rules[p]["type"] == CONJUNCTION:
            configuration[p] = {k: LOW for k in rules[p]["inputs"]}
    button_pushes = 0
    firsts  = list()
    while len(rules_to_find) > 0:
        for r in rules_to_find:
            if configuration[conjunction_to_check][r] == HIGH:
                print(f'Found {r} was HIGH at {button_pushes}')
                rules_to_find.remove(r)
                first.append(button_pushes)
        push_button(configuration, rules)
        button_pushes+=1
    return firsts
        
def part_1(data):
    parsed_data = parse_data(data)
    high, low = get_pulses(parsed_data, 1000)
    total = high * low
    print(f"Part 1: {total}")
    return total

def part_2(data):
    parsed_data = parse_data(data)
    rx_rule = [v for v in parsed_data if 'rx' in  parsed_data[v]['vals']][0]
    assert parsed_data[rx_rule]['type'] == CONJUNCTION # otherwise the problem is easy
    for d in parsed_data[rx_rule]['inputs']:
        print(d, parsed_data[d]['type'])
    factors = find_first_highs_at(parsed_data[rx_rule]['inputs'], parsed_data, rx_rule)
    print(f'Factors are {factors}')
    max_val = max(factors)
    total = max_val
    for i in range(0,10000):#should be enough?
        works = all(total % f == 0 for f in factors)
        if works:
            break
        total += max_val

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
