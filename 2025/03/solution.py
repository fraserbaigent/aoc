from collections import deque

from AocCommon import get_data, get_data_blob, data_to_list_grid, split_data_with_regex

def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")
#data = get_data_blob()
#data = data_to_list_grid()
#data = split_data_with_regex(data, "add pattern")

##########################################################################

def get_joltage(line):
    vals = []
    v = None
    for i in range(0, len(line)-1):
        if v is None or line[i] > line[v]:
            v = i
    v2 = None
    for i in range(len(line) - 1, v, -1):
        if v2 is None or line[i] > line[v2]:
            v2 = i

        
    val = int(f'{line[v]}{line[v2]}')
    return val

def solve_part_1(data):
    total = 0
    for l in data:
        total += get_joltage(l)
    return total

def get_joltage_2(l):
    vals = [int(i) for i in l[-12:]]
    print(l)
    print(vals)
    for i in range(len(l)-13, -1, -1):
        if int(l[i]) >= vals[0]:
            vals.insert(0, int(l[i]))
            ll = len(vals)-1
            for v in range(len(vals) - 2, 0, -1):
                if vals[v] < vals[v+1]:
                    ll = v
            del vals[ll]
    v =  int(''.join([str(c) for c in vals]))

    return v

def solve_part_2(data):
    total = 0
    for l in data:
        total += get_joltage_2(l)
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
