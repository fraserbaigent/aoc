import copy
import json

def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################

routes = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
}


def recurse_from(start, data, visited_grid):
    x, y, score = start
    if (x, y) == (len(data[0]) - 2, len(data) - 1):
        return score
    if (x, y) in visited_grid:
        return None
    visited_grid.add((x, y))

    next_points = list()
    c = data[y][x]
    for r in routes:
        if c in routes and c != r:
            continue
        dx, dy = routes[r]
        x1 = x + dx
        y1 = y + dy
        if y1 < 0 or x1 < 0 or x1 > len(data[0]) or y1 > len(data):
            continue

        cn = data[y1][x1]
        if cn == "#":
            continue

        next_points.append((x1, y1, score + 1))
    if len(next_points) == 0:
        return None
    if len(next_points) == 1:
        return recurse_from(next_points[0], data, visited_grid)
    else:
        max_distance = score
        for n in next_points:
            g = copy.deepcopy(visited_grid)
            next_i = recurse_from(n, data, g)
            if next_i is not None and next_i > max_distance:
                max_distance = next_i
        return max_distance


def iterative_approach_of_doom(data):
    points = [(1, 0, 0, set())]
    max_score = None
    while len(points) > 0:
        x, y, score, grid = points.pop(0)
        if (x, y) == (len(data[0]) - 2, len(data) - 1):
            if max_score is None:
                max_score = score
            elif max_score < score:
                max_score = score
            continue
        elif (x, y) in grid:
            continue
        grid.add((x, y))

        next_points = list()
        c = data[y][x]
        for r in routes:
            if c in routes and c != r:
                continue
            dx, dy = routes[r]
            x1 = x + dx
            y1 = y + dy
            if (
                y1 < 0
                or x1 < 0
                or x1 > len(data[0])
                or y1 > len(data)
                or (x1, y1) in grid
            ):
                continue

            cn = data[y1][x1]
            if cn == "#":
                continue

            next_points.append((x1, y1, score + 1))
        if len(next_points) == 0:
            continue
        elif len(next_points) == 1:
            xn, yn, sn = next_points[0]
            points.append((xn, yn, sn, grid))
        else:
            for n in next_points:
                g = copy.deepcopy(grid)
                xn, yn, sn = n
                points.append((xn, yn, sn, g))
    return max_score

dir_mappings = {
    '>' : '<',
    '^' : 'v',
    'v' : '^',
    '<' : '>',
    }

def part_2_solution(data):
    junctions = [(1, 0)]
    junction_map = dict()
    
    while len(junctions) > 0:
        start_x, start_y = junctions.pop(0)
        junction_joins = [(start_x + routes[d][0], start_y + routes[d][1], d) for d in routes]
        if (start_x,start_y) not in junction_map:
            junction_map[(start_x, start_y)] = dict()
        next_points = [(start_x + routes[d][0], start_y + routes[d][1], d) for d in routes]
            
        for x, y, d in next_points:
            if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data) or data[y][x] == '#' or d in junction_map[(start_x, start_y)]:
                continue
            distance = 1
            pt_queue = [(x,y, d)]
            x_i= y_i= r_i = None
            while len(pt_queue) == 1:
                distance += 1
                x_i, y_i , r_i= pt_queue.pop(0)
                if x_i == len(data[0])-2 and y_i == len(data)-1:
                    break
                for r in routes:
                    if dir_mappings[r_i] == r:
                        continue
                    dx, dy = routes[r]
                    x1 = x_i + dx
                    y1 = y_i + dy
                    if (
                        y1 < 0
                        or x1 < 0
                        or x1 > len(data[0])
                        or y1 > len(data)
                        or data[y1][x1] == '#'
                        ):
                        continue
                    pt_queue.append((x1, y1, r))
            key = (start_x, start_y)
            from_d = dir_mappings[r_i]
            this_key = (x_i,y_i)
            junction_map[key][d] = (this_key, distance-1)
            if this_key not in junction_map:
                junction_map[this_key] = {}
            junction_map[this_key][from_d] = (key, distance-1)
            junctions.append((x_i,y_i))

    refined_junction_map = dict()
    for j in junction_map:
        refined_junction_map[j] = dict()
        for j_i in junction_map[j]:
            key, val = junction_map[j][j_i]
            refined_junction_map[j][key] = val
    return refined_junction_map

def recurse_2(coordinate, end, visited, junction_map,i ):
#    print(f'Recursion depth {i} with coordinate {coordinate}')
    if coordinate in visited:
        return 0
    visited.add(coordinate)
    max_seen = 0
    for c in junction_map[coordinate]:
        if c in visited:
            continue
        d = junction_map[coordinate][c]
        if c == end:
            visited.remove(coordinate)
            return d

        d += recurse_2(c, end, visited, junction_map, i+1)
        if d > max_seen:
            max_seen = d
    visited.remove(coordinate)
    return max_seen
    

def calculate_distance_from(junction_map):
    start_point = (1,0)
    end_point = (len(data[0])-2, len(data)-1)
    return recurse_2(start_point, end_point, set(), junction_map, 0)
    
def find_shortest_route(data):
    start = (1, 0, 0)
    grid = set()
    return recurse_from(start, data, grid)


def part_1(data):
    total = 0#find_shortest_route(data)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    junction_map = part_2_solution(data)
    for j in junction_map:
        print(j, junction_map[j])
    total = calculate_distance_from(junction_map)
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
