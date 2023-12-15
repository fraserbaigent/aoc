def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]

from collections import OrderedDict
data = get_data("data.dat")

##########################################################################
def parse_data(data):
    return data.split(',')

def hash_string(string):
    val = 0
    for c in string:
        val += ord(c)
        val *= 17
        val %= 256
        
    return val

def part_1(data):
    total = 0
    parsed = parse_data(data[0])
    for p in parsed:
        total += hash_string(p)
    print(f"Part 1: {total}")
    return total

import re
def part_2(data):
    total = 0
    reg = re.compile('^([a-z]+)([-=])(\\d+)?$')
    parsed = parse_data(data[0])
    grid = dict()
    for i in range(0,256):
        grid[i] = {
            'names':[],
            'values':[],
            }
        
    for p in parsed:
        m = reg.match(p)
        raw_string = m.groups()[0]             
        symbol = m.groups()[1]
        count = m.groups()[2] if len(m.groups()) > 2 else None
        hashed = hash_string(raw_string)
        current = grid[hashed]
        if symbol == '-':
            if raw_string in current['names']:
                i = current['names'].index(raw_string)
                del current['names'][i]
                del current['values'][i]
        elif symbol =='=':
            if raw_string in current['names']:
                i = current['names'].index(raw_string)
                current['values'][i] = count
            else:
                current['values'].append(count)
                current['names'].append(raw_string)
    for g in grid:
        if len(grid[g]['names']):
            print(f'{g}: {grid[g]}')
        i = int(g)
        b = grid[g]
        for j, k in enumerate(b['values']):
            val= (i+1) * (j+1) * int(k)
            total+=val
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
