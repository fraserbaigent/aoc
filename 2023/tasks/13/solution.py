def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_data(data):
    patterns = list()
    pattern = []
    for d in data:
        if len(d) == 0:
            if len(pattern):
                patterns.append(pattern)
            pattern = []
        else:
            pattern.append([d_i for d_i in d])
    if len(pattern):
        patterns.append(pattern)
    return patterns


def get_vertical_score(pattern):
<<<<<<< HEAD
    indices = [i for i in range(1, len(pattern[0]))]
=======
    indices = [i for i in range(1, len(pattern[0]) - 1)]
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)
    for row in pattern:
        index = 0
        while index < len(indices):
            l = indices[index] - 1
            r = indices[index]
            while True:
                if row[l] != row[r]:
                    indices.pop(index)
                    index -= 1
                    break
                l -= 1
                r += 1
                if l < 0 or r == len(pattern[0]):
<<<<<<< HEAD
                    break
            index += 1

    for i in to_ignore:
        if i in indices:
            indices.remove(i)
=======
                    return indices[index]
            index += 1
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)
    found_index = indices[0] if len(indices) == 1 else 0
    return found_index


<<<<<<< HEAD
def get_horizontal_score(pattern, to_ignore=list()):
=======
def get_horizontal_score(pattern):
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)
    indices = [i for i in range(1, len(pattern))]
    for col_i in range(0, len(pattern[0])):
        index = 0
        while index < len(indices):
            t = indices[index] - 1
            b = indices[index]
            while True:
                if pattern[t][col_i] != pattern[b][col_i]:
                    indices.pop(index)
                    index -= 1
                    break
                t -= 1
                b += 1
<<<<<<< HEAD
                if t < 0 or b >= len(pattern):
                    break
            index += 1
    for i in to_ignore:
        if i in indices:
            indices.remove(i)
=======
                if t < 0 or b == len(pattern):
                    return indices[index]
            index += 1
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)
    found_index = indices[0] if len(indices) == 1 else 0

    return found_index


<<<<<<< HEAD
def get_pattern_score(pattern):
    vertical = get_vertical_score(pattern)
    horizontal = 100 * get_horizontal_score(pattern)
=======

def get_pattern_score(pattern, i):
    vertical = get_vertical_score(pattern)
    horizontal = get_horizontal_score(pattern)
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)
    if vertical > 0 and horizontal > 0:
        raise Exception(f"{i+1}: V={vertical}, H={horizontal}")
    return vertical + horizontal


<<<<<<< HEAD
def get_pattern_score_2(pattern, i):
    original_v = get_vertical_score(pattern)
    original_h = get_horizontal_score(pattern)
    for x in range(0, len(pattern[0]) - 1):
        for y in range(0, len(pattern)):
            char = pattern[y][x]
            to_char = "." if char == "#" else "#"
            pattern[y][x] = to_char

            v = get_vertical_score(pattern, [original_v])
            h = get_horizontal_score(pattern, [original_h])

            if v > 0 and v != original_v:
                print(
                    f"{x},{y} flipped from {char} to {to_char} on pattern {i} giving a v score of {v} - original was {original_v}, {original_h}"
                )
                return v
            elif h > 0 and h != original_h:
                print(
                    f"{x},{y} flipped from {char} to {to_char} on pattern {i} giving a h score of {h} - original was {original_v}, {original_h}"
                )
                return 100 * h
            pattern[y][x] = char

    print(f"Pattern {i} was a yikes!")


def part_1(data):
    total = 0
    patterns = parse_data(data)
    for p in patterns:
        res = get_pattern_score(p)
=======
def part_1(data):
    total = 0
    patterns = parse_data(data)
    for i, p in enumerate(patterns):
        res = get_pattern_score(p, i)
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)
        total += res
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
<<<<<<< HEAD
    patterns = parse_data(data)
    for i, p in enumerate(patterns):
        res = get_pattern_score_2(p, i)
        total += res
=======
>>>>>>> 8cf47fa (Added tests - think algorithm isn't doing edge cases)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
