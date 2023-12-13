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


def get_vertical_score(pattern, to_ignore=[]):
    indices = [i for i in range(1, len(pattern[0]))]
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

                    break
            index += 1

    for i in to_ignore:
        if i in indices:
            indices.remove(i)
            return indices[index]
            index += 1
    found_index = indices[0] if len(indices) == 1 else 0
    return found_index


def get_horizontal_score(pattern, to_ignore=list()):
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
                if t < 0 or b >= len(pattern):
                    break
            index += 1
    for i in to_ignore:
        if i in indices:
            indices.remove(i)
            if t < 0 or b == len(pattern):
                return indices[index]
            index += 1
    found_index = indices[0] if len(indices) == 1 else 0

    return found_index


def get_pattern_score(pattern, i):
    vertical = get_vertical_score(pattern)
    horizontal = 100 * get_horizontal_score(pattern)
    if vertical > 0 and horizontal > 0:
        raise Exception(f"{i + 1}: V={vertical}, H={horizontal}")

    return vertical + horizontal


def pt2(grid, vertical):
#    print(f"Width = {len(grid[0])}, height = {len(grid)}")

    to_check = grid[0] if vertical else grid
    to_iterate = grid if vertical else grid[0]
    indices = [i for i in range(1, len(to_iterate))]
    good_indices = {i:[] for i in indices}    
    for j in range(0, len(to_check)):
        for i in indices:
            index = 0
            good = True
            while True:
                left = i - index - 1
                right = index + i
                if left < 0 or right >= len(to_iterate):
                    break
                left_e = grid[left][j] if vertical else grid[j][left]
                right_e = grid[right][j] if vertical else grid[j][right]                
                
                if left_e != right_e:
                    good = False
                    break
                index += 1
            if good == True:
#                print(f"{j} : {i} is good")
                good_indices[i].append(j)
    trials = {g: v for g, v in good_indices.items() if len(v) == len(to_check) - 1}
    if len(trials.keys()) > 1:
        print('\n'.join([''.join(p_i) for p_i in grid]))
        print(good_indices)
        print(vertical)
        raise Exception("!!!")
    elif len(trials.keys()) ==1:
        return list(trials.keys())[0] * (100 if vertical else 1)
        
    return 0


def get_pattern_score_2(pattern, i):
    original_v = get_vertical_score(pattern)
    original_h = get_horizontal_score(pattern)
    for x in range(0, len(pattern[0]) - 1):
        for y in range(0, len(pattern) - 1):
            char = pattern[y][x]
            to_char = "." if char == "#" else "#"
            pattern[y][x] = to_char

            v = get_vertical_score(pattern, [original_v])
            h = get_horizontal_score(pattern, [original_h])
            pattern[y][x] = char

            if v > 0 and v != original_v:
                return v
            elif h > 0 and h != original_h:
                return 100 * h


def part_1(data):
    total = 0
    patterns = parse_data(data)
    for i, p in enumerate(patterns):
        res = get_pattern_score(p, i)
        total += res
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    patterns = parse_data(data)
    for v in [True, False]:
        for i, p in enumerate(patterns):
            res = pt2(p, v)
            total += res

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    #    part_1(data)
    part_2(data)
