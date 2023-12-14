import copy
import os
import re
import sys

import requests


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


def to_submit() -> str:
    if len(sys.argv) == 1:
        return False, False
    elif len(sys.argv) > 3:
        print(f"Too many arguments")
        sys.exit(1)
    return "s1" in sys.argv, "s2" in sys.argv


def get_cookie() -> str:
    with open("../../.cookie_secret", "r") as infile:
        return infile.read()


def get_date_data() -> tuple:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    regex = re.compile("^.*/(\\d{4})/(\\d{2})$")
    res = regex.match(current_file_directory)
    return res.groups()[0], res.groups()[1]


def submit(answer, question):
    year, day = get_date_data()
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    session_cookie = get_cookie()
    headers = {
        "User-Agent": "YourCustomUserAgentHere",
        "Cookie": f"session={session_cookie}",
    }
    payload = f"level={question}&answer={answer}"
    response = requests.post(url, data=payload, headers=headers)
    print(f"Response: {response.status_code}: \n", response.text)


data = get_data("data.dat")

##########################################################################


def get_lines(index, data) -> list:
    lines = list()
    line_start = -1
    boulders = 0
    for i, d in enumerate(data):
        c = d[index]
        if c == "O":
            boulders += 1
        elif c == "#":
            if boulders > 0:
                lines.append([line_start + 1, boulders])
            line_start = i
            boulders = 0
    if boulders > 0:
        lines.append([line_start + 1, boulders])

    return lines


def get_score_for_line(line, row_zero_score) -> int:
    start_score = row_zero_score - line[0]
    total = 0
    for j, i in enumerate(range(line[0], line[0] + line[1])):
        total += start_score - j
    return total


def get_scores_for_lines(lines, row_zero_score) -> int:
    return sum([get_score_for_line(line, row_zero_score) for line in lines])


def get_score_for_col(index, data) -> int:
    lines = get_lines(index, data)
    return get_scores_for_lines(lines, len(data))


def rotate(data, direction) -> list:
    if direction == "N":
        for i in range(0, len(data[0])):
            line_start = -1
            boulders = 0
            for j in range(0, len(data)):
                c = data[j][i]
                if c == "O":
                    boulders += 1
                elif c == "#":
                    for b in range(line_start + 1, j):
                        if b - line_start <= boulders:
                            data[b][i] = "O"
                        else:
                            data[b][i] = "."
                    line_start = j
                    boulders = 0
            for b in range(line_start + 1, len(data)):
                if b - line_start <= boulders:
                    data[b][i] = "O"
                else:
                    data[b][i] = "."
    elif direction == "S":
        for i in range(0, len(data[0])):
            line_start = len(data)
            boulders = 0
            for j in range(len(data) - 1, -1, -1):
                c = data[j][i]
                if c == "O":
                    boulders += 1
                elif c == "#":
                    for b in range(line_start - 1, j, -1):
                        if line_start - b <= boulders:
                            data[b][i] = "O"
                        else:
                            data[b][i] = "."
                    line_start = j
                    boulders = 0
            for b in range(line_start - 1, -1, -1):
                if line_start - b <= boulders:
                    data[b][i] = "O"
                else:
                    data[b][i] = "."

    elif direction == "W":
        for i in range(0, len(data)):
            line_start = -1
            boulders = 0
            for j in range(0, len(data[i])):
                c = data[i][j]
                if c == "O":
                    boulders += 1
                elif c == "#":
                    for b in range(line_start + 1, j):
                        if b - line_start <= boulders:
                            data[i][b] = "O"
                        else:
                            data[i][b] = "."
                    line_start = j
                    boulders = 0

            for b in range(line_start + 1, len(data[i])):
                if b - line_start <= boulders:
                    data[i][b] = "O"
                else:
                    data[i][b] = "."
    elif direction == "E":
        for i in range(0, len(data)):
            line_start = len(data[i])
            boulders = 0
            for j in range(len(data[i]) - 1, -1, -1):
                c = data[i][j]
                if c == "O":
                    boulders += 1
                elif c == "#":
                    for b in range(line_start - 1, j, -1):
                        if line_start - b <= boulders:
                            data[i][b] = "O"
                        else:
                            data[i][b] = "."
                    line_start = j
                    boulders = 0
            for b in range(line_start - 1, -1, -1):
                if line_start - b <= boulders:
                    data[i][b] = "O"
                else:
                    data[i][b] = "."
    return data


def hash_it(adjusted_data: list) -> str:
    v = []
    for a in adjusted_data:
        v += a
    return hash(tuple(v))


def adjust_data(data, cycles) -> list:
    data_cache = {}
    cache_ref = {}
    directions = [
        "N",
        "W",
        "S",
        "E",
    ]
    i = 0
    adjusted = copy.deepcopy(data)

    while i < cycles:
        hashed = hash_it(adjusted)
        if hashed in data_cache:
            i, adjusted = lookup_from_cache(i, data_cache, cache_ref, hashed, cycles)
        else:
            data_cache[hashed] = i
            cache_ref[i] = copy.deepcopy(adjusted)

            for d in directions:
                adjusted = rotate(adjusted, d)

        i += 1
    return adjusted


def lookup_from_cache(i, data_cache, cache_ref, hashed, cycles) -> tuple:
    index = data_cache[hashed]
    since_then = i - index
    to_end = cycles - i
    remainder = to_end % since_then
    trial_end = index + remainder
    if trial_end in cache_ref:
        return cycles, cache_ref[trial_end]
    else:
        i = cycles - remainder
        return i, cache_ref[index]


def data_to_matrix(data) -> list:
    matrix = []
    for d in data:
        matrix.append([])
        for c in d:
            matrix[-1].append(c)
    return matrix


def get_score_for(grid):
    total = 0
    for i, r in enumerate(grid):
        total += (len(grid) - i) * sum([1 for r_i in r if r_i == "O"])
    return total


def part_1(data, to_submit) -> int:
    this_data = data_to_matrix(data)
    this_data = rotate(this_data, "N")
    total = get_score_for(this_data)

    if to_submit == True:
        submit(total, 1)
    print(f"Part 1: {total}")
    return total


def part_2(data, to_submit) -> int:
    this_data = data_to_matrix(data)
    adjusted_data = adjust_data(this_data, 1000000000)
    total = get_score_for(adjusted_data)

    if to_submit == True:
        submit(total, 2)
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    submit_1, submit_2 = to_submit()
    part_1(data, submit_1)
    part_2(data, submit_2)
