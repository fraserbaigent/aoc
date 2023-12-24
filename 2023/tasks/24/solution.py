import re

import numpy as np
from numpy.random import uniform


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data):
    rx = re.compile("^(\\d+), +(\\d+), +(\\d+) +\\@ +(-?\\d+), +(-?\\d+), +(-?\\d+)$")

    hails = list()
    for d in data:
        res = rx.match(d)
        hails.append(tuple([int(i) for i in res.groups()]))
    return hails


def get_x(ya0, yb0, xa0, xb0, vya, vyb, vxa, vxb):
    m1 = vya / vxa
    m2 = vyb / vxb

    if m1 == m2:
        return None
    return (ya0 - yb0) / (m2 - m1) + (xb0 * m2 - xa0 * m1) / (m2 - m1)


def get_y(y0, vy, vx, x0, x):
    """
    x = x0 + vx*t
    y = y0 + vy*t
    t = (x - x0) / vx
    t = (y - y0) / vy
    1 = ((x - x0) * vy) / ((y -y0) * vx) )
    y - y0 = (x - x0) * vy / vx
    y = y0 + (x - x0)* vy / vx

    """

    if vx == 0:
        return None
    return y0 + (vy / vx) * (x - x0)


def get_t(x1, x0, vx):
    if vx == 0:
        return -1
    return (x1 - x0) / vx


def get_intersection_coordinate(pt1, pt2):
    x0, y0, z0, vx0, vy0, vz0 = pt1
    x1, y1, z1, vx1, vy1, vz1 = pt2

    x_i = get_x(y0, y1, x0, x1, vy0, vy1, vx0, vx1)
    if x_i is None:
        return None, None
    y_i = get_y(y0, vy0, vx0, x0, x_i)

    t1 = get_t(x_i, x0, vx0)
    t2 = get_t(x_i, x1, vx1)
    if t1 < 0 or t2 < 0:
        return None, None
    return (x_i, y_i)


def part_1(data, bounds=(200000000000000, 400000000000000)):
    total = 0
    parsed = parse_data(data)
    for i in range(0, len(parsed)):
        for j in range(i + 1, len(parsed)):
            x, y = get_intersection_coordinate(parsed[i], parsed[j])
            if x is not None and y is not None:
                if (
                    x >= bounds[0]
                    and x <= bounds[1]
                    and y >= bounds[0]
                    and y <= bounds[1]
                ):
                    total += 1
    print(f"Part 1: {total}")
    return total


class Point:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    """
    x = x0 + tv
    x0' + tv' = x0+tv
    t(v'-v) = x0-x0'
    t = (x0-x0') / (v'-v)
    """

    def t_x(self, x, v):
        if v == self.vx:
            return None
        return (self.x - x) / (v - self.vx)

    def t_y(self, y, v):
        if v == self.vy:
            return None

        return (self.y - y) / (v - self.vy)

    def t_z(self, z, v):
        if v == self.vz:
            return None

        return (self.z - z) / (v - self.vz)

    def get_delta_for(self, x, v):
        total = 0
        times = [
            self.t_x(x[0], v[0]),
            self.t_y(x[1], v[1]),
            self.t_z(x[2], v[2]),
        ]
        if any(t is None for t in times):
            return None

        for i in range(0, 3):
            for j in range(i, 3):
                total += abs(times[i] - times[j])
        return total


def get_limits(parsed_data):
    min_x = max_x = None
    min_y = max_y = None
    min_z = max_z = None

    min_vx = max_vx = None
    min_vy = max_vy = None
    min_vz = max_vz = None

    for x, y, z, vx, vy, vz in parsed_data:
        if min_x is None or x < min_x:
            min_x = x
        if max_x is None or x > max_x:
            max_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_y is None or y > max_y:
            max_y = y
        if min_z is None or z < min_z:
            min_z = z
        if max_z is None or z > max_z:
            max_z = z

        if min_vx is None or vx < min_vx:
            min_vx = vx
        if max_vx is None or vx > max_vx:
            max_vx = vx
        if min_vy is None or vy < min_vy:
            min_vy = vy
        if max_vy is None or vy > max_vy:
            max_vy = vy
        if min_vz is None or vz < min_vz:
            min_vz = vz
        if max_vz is None or vz > max_vz:
            max_vz = vz

    return (
        (
            (min_x - 1, max_x + 1),
            (min_y - 1, max_y + 1),
            (min_z - 1, max_z + 1),
        ),
        (
            (-10, 10),
            (-10, 10),
            (-10, 10),
        ),
    )


def initial_temperature(probability, x_bar):
    return -x_bar / np.log(probability)


def sa(e_best, e, temperature):
    return np.exp((e_best - e) / temperature)


def perturbate(initial, limits, scaling_factor):
    if initial is None:
        return tuple([(l[1] + l[0]) / 2 for l in limits])
    INITIAL_SCALE = 0.30
    points = []
    i = 0
    while len(points) < len(initial):
        span = limits[i][1] - limits[i][0]
        val = initial[i]
        trials = 0
        while True or trials < 100:
            delta = uniform(-1.0, 1.0) * span * INITIAL_SCALE / scaling_factor
            if val + delta > limits[i][0] and val + delta < limits[i][1]:
                break
            trials += 1
        if trials >= 5:
            delta = 0
        points.append(int(val + delta))
        i += 1
    return tuple(points)


def part_2(data):
    allowed_limit = 1000000
    temperature_step = allowed_limit / 20
    t = initial_temperature(0.8, 350037827103328.2)
    total = 0
    parsed_data = parse_data(data)
    points = [Point(*p) for p in parsed_data]
    nearest_delta = None
    nearest_x = None
    nearest_v = None
    i = 0
    x_limits, v_limits = get_limits(parsed_data)
    delta_averages = [0, 0]
    last_x = last_v = None
    while True:
        if i % 100 == 0:
            print(f"Progress: {i / allowed_limit * 100.0:>6.02f}%", end="\r")

        i += 1
        if i > allowed_limit:
            print(
                f"\nFailed to find anything - nearest was {nearest_delta} with {nearest_x}, {nearest_v}"
            )
            break
        trial_x = perturbate(last_x, x_limits, 1)
        trial_v = perturbate(last_v, v_limits, 1)
        trial_total = 0
        is_bad = False
        for p in points:
            this_total = p.get_delta_for(trial_x, trial_v)
            if this_total is None:
                is_bad = True
                break
            trial_total += this_total
        if is_bad:
            continue
        if nearest_delta is not None:
            delta_averages[0] += abs(nearest_delta - trial_total)
            delta_averages[1] += 1

        if trial_total == 0:
            total = trial_x[0] * trial_x[1] * trial_x[2]
            answer = trial_x
            answer_v = trial_v
            break
        elif nearest_delta is None or trial_total < nearest_delta:
            nearest_x = last_x = trial_x
            nearest_v = last_v = trial_v
            nearest_delta = trial_total

        else:
            sa_score = sa(nearest_delta, trial_total, t)
            if uniform(0, 1.0) < sa_score:
                last_x = trial_x
                last_v = trial_v
        if i % temperature_step == 0:
            t /= 4

    print(f"\nThe average total here was {delta_averages[0] / delta_averages[1]}")
    print(f"Found after {i} iterations:\nx = {trial_x}\nv = {trial_v}")
    return total


test_data = [
    l.strip()
    for l in """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".split(
        "\n"
    )
    if len(l.strip())
]

if __name__ == "__main__":
    #    part_1(data)
    part_2(test_data)
