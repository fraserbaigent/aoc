from AocCommon import get_data, data_to_list_grid

data = get_data()
data = data_to_list_grid(data, ty = int)

##########################################################################

DIRS = [(-1,0),(1,0),(0,1),(0,-1)]

def solve_part_1(data):
    memo = [[None for i in d] for d in data]
    total = 0
    for y, d in enumerate(data):
        for x, d_i in enumerate(d):
            if d_i == 0:
                v = recurse((x,y), None, memo, data)
                total += len(v[0])
    return total

def recurse(coord, direction, memo, grid):
    x0,y0 = coord
    total = 0
    if grid[y0][x0] == 9:
        memo[y0][x0] = (set([(x0,y0)]), 1)
    
    if memo[y0][x0] is not None:
        return memo[y0][x0]

    ends = set()
    total = 0
    for dx, dy in DIRS:
        if direction is not None and (-dx,-dy) == direction:
            continue
        x = x0 + dx
        y = y0 + dy
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            continue

        if grid[y][x] == grid[y0][x0] + 1:
            v, t = recurse((x,y), (dx,dy), memo, grid)
            for v_i in v:
                ends.add(v_i)
            total += t
    memo[y0][x0] = (ends, total)
    return ends, total
        

def solve_part_2(data):
    memo = [[None for i in d] for d in data]
    total = 0
    for y, d in enumerate(data):
        for x, d_i in enumerate(d):
            if d_i == 0:
                v = recurse((x,y), None, memo, data)
                total += v[1]
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
