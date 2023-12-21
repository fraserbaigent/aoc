def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################
def find_start(data):
    for y,d in enumerate(data):
        for x, d_i in enumerate(d):
            if d_i == 'S':
                return (x,y)

def recurse(x0,y0,steps,step_limit,cache):           
    cache[(x0,y0)] = steps
    if steps == step_limit:
        return

    for (dy,dx) in [(0,1),(0,-1),(-1,0),(1,0)]:
        x = x0+dx
        y = y0+dy
        if (((x,y) not in cache or cache[(x,y)] > steps+1)
            and x >= 0
            and x < len(data[0])
            and y >= 0
            and y < len(data)
            and data[y][x] != '#'):
            recurse(x,y, steps+1,step_limit, cache)
            
def recurse_2(x0,y0,steps,step_limit,cache):           
    cache[(x0,y0)] = steps
    if steps == step_limit:
        return

    for (dy,dx) in [(0,1),(0,-1),(-1,0),(1,0)]:
        x = x0+dx % len(data[0])
        y = y0+dy % len(data)
        if (((x,y) not in cache or cache[(x,y)] > steps+1)
            and data[y][x] != '#'):
            recurse(x0+dx,y0+dy, steps+1,step_limit, cache)

def part_1(data, step_count):
    total = 0
    visited = dict()
    x, y = find_start(data)
    recurse(x,y,0,step_count, visited)

    for v in visited:
        if visited[v] % 2 == 0:
            total+=1
            
    print(f"Part 1: {total}")
    return total


def part_2(data, step_count):
    total = 0
    visited = dict()
    x, y = find_start(data)
    recurse(x,y,0,step_count, visited)

    for v in visited:
        if visited[v] % 2 == 0:
            total+=1
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data, 64)
    part_2(data, 26501365)
