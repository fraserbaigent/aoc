import math
import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def distance_calculation(time_to_beat, distance_to_beat, acceleration):
    # D = v * t
    # D = (v' * t_c ) * ( t_0 - t_c)
    # D = v' * t_0 * t_c - v' * t_c ^2
    # -v' t_c^2 + v' * t_0 t_c - D = 0
    a = -acceleration
    b = acceleration * time_to_beat
    c = -distance_to_beat + 1

    def x_l(a, b, c):
        return math.ceil((-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a))

    def x_r(a, b, c):
        return math.floor((-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a))

    r = x_r(a, b, c)
    l = x_l(a, b, c)

    def distance(t):
        return (time_to_beat - t) * t * acceleration

    if distance(r) == distance_to_beat:
        r -= 1
    if distance(l) == distance_to_beat:
        l += 1

    return l, r


def parse_data(data):
    re_time = re.compile("Time:(.*)$")
    re_distance = re.compile("Distance:(.*)$")

    time_res = re_time.match(data[0])
    distance_res = re_distance.match(data[1])

    parsed = list()
    for t, d in zip(
        time_res.groups()[0].strip().split(),
        distance_res.groups()[0].strip().split(),
    ):
        parsed.append([int(t.strip()), int(d.strip())])
    return parsed

def parse_data_pt2(data):
    re_time = re.compile("Time:(.*)$")
    re_distance = re.compile("Distance:(.*)$")


    time_res = int(re_time.match(data[0]).groups()[0].replace(' ','').strip())
    distance_res = int(re_distance.match(data[1]).groups()[0].replace(' ','').strip())    

    return [time_res, distance_res]
def part_1(data):
    total = 1
    races = parse_data(data)
    for r in races:
        l, r = distance_calculation(r[0], r[1], 1)
        total *= abs(r - l) + 1
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 1
    races = parse_data_pt2(data)
    l, r = distance_calculation(races[0], races[1], 1)
    total *= abs(r - l) + 1

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
