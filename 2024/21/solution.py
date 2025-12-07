def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def get_routes(pt1, pt2):
    deltas = {
        "v": (0, 1),
        "^": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }
    x2, y2 = pt2
    routes = [(pt1, "")]
    answers = []
    while len(routes):
        pt, s = routes.pop(0)
        x, y = pt
        if x == x2 and y == y2:
            answers.append(s)
            continue
        for v, (dx, dy) in deltas.items():
            xx = x + dx
            yy = y + dy
            if (abs(y2 - yy) > abs(y2 - y)) or (abs(x2 - xx) > abs(x2 - x)):
                continue
            routes.append(((xx, yy), s + v))
    max_len = len(sorted(answers, reverse=True)[0])
    return [a for a in answers if len(a) == max_len]


def get_shortest_route_map(buttons):
    all_routes = {b: {b_i: [] for b_i in buttons} for b in buttons}
    for b, c in buttons.items():
        for b_o, c_o in buttons.items():
            all_routes[b][b_o] += get_routes(c, c_o)
    return all_routes


def get_pad_map(numpad):
    pad_map = {}
    for y, row in enumerate(numpad.split("\n")):
        for x, c in enumerate(row):
            if c != "X":
                pad_map[c] = (x, y)
    return pad_map


def get_robot_routes(code, robot_data):
    if len(code) == 0:
        return ['']
    position, mapping = robot_data    

    route = []
    for i in range(len(code), 0, -1):
        test_code = code[:i]
        if test_code in mapping[position]:
            if len(test_code) > 1:
                print(f'Cache hit! ({len(test_code)})')
            route.append(mapping[position][test_code])
            if i == len(code):
                new_code = ""
                new_position = 0
            else:
                new_code = code[i:]
                new_position = code[i-1]
            break
        
    route.append(get_robot_routes(new_code, (new_position, mapping)))
    expanded_routes = route[0]
    for r in route[1:]:
        pending = []        
        for n in r:
            for e in expanded_routes:
                pending.append(e + 'A' + n)
        expanded_routes = pending
    mapping[position][code] = expanded_routes
    return expanded_routes


def get_all_routes(robot, data):
    routes = []
    for d in data:
        routes+= get_robot_routes(d, robot)

    return routes


def solve_part_1(data):
    numpad = "789\n456\n123\nX0A"
    numpad_map = get_pad_map(numpad)
    arrow_map = get_pad_map("X^A\n<v>")
    shortest_numpad_routes = get_shortest_route_map(numpad_map)
    shortest_arrow_map = get_shortest_route_map(arrow_map)

    robot_1 = ("A", shortest_numpad_routes)  # numpad
    robot_2 = ("A", shortest_arrow_map)  # radioactive
    robot_3 = ("A", shortest_arrow_map)  # frozen
    robot_4 = ("A", shortest_arrow_map)  # me

    cache = {}
    score = 0
    for d in data:
        robot_1_routes = get_all_routes(robot_1, [d])
        robot_2_routes = get_all_routes(robot_2, robot_1_routes)
        total = 0
        total = 0        
        for v in shortest_arrow_map.values():
            for v_i in v.values():
                total += len(v_i)

        print(len(robot_2_routes), total)
        robot_3_routes = get_all_routes(robot_3, robot_2_routes)
        total = 0        
        for v in shortest_arrow_map.values():
            for v_i in v.values():
                total += len(v_i)
        
        print(len(robot_3_routes), total)
        break
#        score += len(robot_4_routes[0]) * int(d[:-1])

    return score


def solve_part_2(data):
    pass


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
