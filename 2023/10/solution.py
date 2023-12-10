def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


##########################################################################

elements = {
    "|": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "-": [(1, 0), (-1, 0)],
    "J": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "F": [(-1, 0), (0, -1)],
    ".": [],
    "S": [],
}


def find_start(data):
    for i, d in enumerate(data):
        for j, dd in enumerate(d):
            if dd == "S":
                return (j, i)

def get_surrounding_spots(coordinate, to_direction, data):
    x, y = coordinate
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return list()
    symbol = data[y][x]

    if symbol == "." or (symbol != "S" and to_direction not in elements[symbol]):
        return list()

    points = list()
    for direction in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        m = (-direction[0], -direction[1])
        if m == to_direction:
            continue
        if symbol == "S" or m in elements[symbol]:
            points.append(((x, y), direction))
    return points


def solve_with(start_coordinate, data):
    next_spots = get_surrounding_spots(start_coordinate, None, data)
    distances = {start_coordinate: 0}
    while len(next_spots) > 0:
        coordinate, direction = next_spots.pop(0)
        next_coordinate = (coordinate[0] + direction[0], coordinate[1] + direction[1])
        if next_coordinate in distances:
            break

        spots_to_add = get_surrounding_spots(next_coordinate, direction, data)
        if len(spots_to_add) > 0:
            distances[next_coordinate] = distances[coordinate] + 1
            next_spots += spots_to_add
    return distances

def get_pt2_result(rows):
    total = 0
    for column_index in range(0, len(rows[0])):
        counting = False
        previous = None
        pairs = list()
        for i in range(0, len(rows)):
            pipe = rows[i][column_index]
            if column_index == 611:
                print(f'{pipe} {i} {len(pairs)} {counting} {previous}')
            
            if pipe == "|":
                continue
            elif pipe == "-":
                counting = not counting
            elif pipe in ["7", "F"]:
                previous = pipe
            elif pipe == "J":
                if previous == "F":
                    counting = not counting
                pairs.append([previous, pipe])                    
                previous = None
            elif pipe == "L":
                if previous == "7":
                    counting = not counting
                pairs.append([previous, pipe])
                previous = None
            elif counting:
                rows[i][column_index] = 'X'
                total += 1
    for i, v in enumerate(rows[-1]):
        if v == 'X':
            break
    for r in rows:
        print(''.join(r))
    return total

def get_start_point_type(start_coordinate, data, pipe_coordinates):
    trials = get_surrounding_spots(start_coordinate, None, data)
    directions_ok = []
    for t in trials:
        x = t[0][0] + t[1][0]
        y = t[0][1] + t[1][1]
        pipe = data[y][x]
        if t[1] in elements[pipe]:
            directions_ok.append((-t[1][0], -t[1][1]))
    for e,v in elements.items():
        if v == directions_ok:
            return e
    return None

def get_grid(distances, raw_data):
    grid = [['.' for r in row] for row in raw_data]
    for d in distances:
        pipe = raw_data[d[1]][d[0]]
        grid[d[1]][d[0]] =  pipe
    start = find_start(raw_data)
    grid[start[1]][start[0]] = get_start_point_type(start, raw_data, list(distances.keys()))
        
    return grid

def part_1(data):
    start = find_start(data)
    distances = solve_with(start, data)
    total = max(distances.values())
    print(f"Part 1: {total}")
    return total

def part_2(data):
    start = find_start(data)
    distances = solve_with(start, data)
    grid = get_grid(distances, data)
    total = get_pt2_result(grid)
    print(f"Part 2: {total}")
    return total
    
if __name__ == "__main__":
    data = get_data("data.dat")

    part_1(data)
    part_2(data)
