def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return infile.readlines()


def from_beginning(string):
    zero = ord("0")
    nine = ord("9")
    for i in string:
        v = ord(i)
        val = v - zero
        if val >= 0 and val <= 10:
            return i


def from_end(string):
    zero = ord("0")
    nine = ord("9")
    for i in reversed(string):
        v = ord(i)
        val = v - zero
        if val >= 0 and val <= 10:
            return i


def from_beginning_2(string, reverse=False):
    digit_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
    string = string.lower()
    if reverse:
        string = string[::-1]
        keys = [k for k in digit_map.keys()]
        for d in keys:
            k = digit_map[d]
            new_d = d[::-1]
            del digit_map[d]
            digit_map[new_d] = k

    results = dict()
    for k in digit_map.keys():
        i = string.find(k)
        if i >= 0:
            results[k] = i
    digit = sorted(results.keys(), key=lambda k: results[k])[0]
    return str(digit_map[digit])


def part_1():
    data_file = "data.dat"
    data = get_data(data_file)
    tot = 0
    for l in data:
        vs = from_beginning(l) + from_end(l)
        tot += int(vs)
    print(f"Part 1: {tot}")


def part_2():
    data_file = "data.dat"
    data = get_data(data_file)
    tot = 0
    for l in data:
        l = l.strip()
        vs = from_beginning_2(l) + from_beginning_2(l, True)
        tot += int(vs)
    print(f"Part 2: {tot}")


part_1()
part_2()
