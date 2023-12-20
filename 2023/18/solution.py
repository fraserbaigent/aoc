import copy
import re
from functools import cmp_to_key
from AocCommon import get_data, split_data_with_regex

data = split_data_with_regex(get_data(),
                             "^(\\w) (\\d+) \\(\\#(\\w+)(\\d{1})\\)$",
                             types = (str, int, str, int),)

##########################################################################

def get_lines(instructions):
    x = 0
    y = 0

    dl = {
        "L": [-1, 0],
        "R": [1, 0],
        "U": [0, -1],
        "D": [0, 1],
    }
    lines = list()
    for instruction in instructions:
        dx, dy = dl[instruction[0]]
        x_n = x + dx * instruction[1]
        y_n = y + dy * instruction[1]
        lines.append([[x, y], [x_n, y_n], instruction[2]])
        y = y_n
        x = x_n
    return lines

def find_start(grid):
    for i,r in enumerate(grid[0]):
        if r == '#' and grid[1][i] is None:
            return (i, 1)

        
def flood_fill(grid, start_x, start_y):
    stack = [(start_x, start_y)]
    count=0
    while len(stack) > 0:
        count+=1
        x,y = stack.pop()
        grid[y][x]='o'
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            elif grid[ny][nx] is not None:
                continue
            stack.append((nx,ny))
    return grid

def part_1(parsed_data):
    lines = get_lines(parsed_data)
    a = shoelace(lines)
    p = perimeter(lines)
    total = a + (p//2) + 1    
    print(f'Part 1: {total}')
    return total

def get_lines_2(data):
    dir_map = ['R','D','L','U']
    x = 0
    y = 0
    lines = list()
    dirs = {
        'R' : (1,0),
        'L' : (-1,0),
        'U' : (0,1),
        'D' : (0, -1),
        }
    for d in data:
        v = int(d[2], 16)
        d = dir_map[d[3]]
        m = dirs[d]
        dx = m[0] * v
        dy = m[1] * v
        nx = x+dx
        ny = y+dy
        lines.append(((x,y),(nx,ny)))
        x = nx
        y = ny
    return lines
    
        
def shoelace(lines):
    area = 0
    for i, l in enumerate(lines):
        x1,y1 = l[0]
        x2,y2 = l[1]
        diff = x1*y2 - y1*x2
        area += diff
    return abs(area) // 2

def perimeter(lines):
    perimeter = 0
    for l in lines:
        for i in [0,1]:
            perimeter += abs(l[1][i] - l[0][i])
    return int(perimeter)

def part_2(data):
    total = 0
    lines = get_lines_2(data)
    area = shoelace(lines)
    p = perimeter(lines)
    total = area + (p//2) + 1
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
