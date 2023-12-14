def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def get_lines(index, data):
    lines = list()
    line_start = -1
    boulders = 0
    for i, d in enumerate(data):
        c = d[index]
        if c == "O":
            boulders += 1
        elif c == "#":
            if boulders > 0:
                lines.append([line_start + 1, boulders])
            line_start = i
            boulders = 0
    if boulders > 0:
        lines.append([line_start + 1, boulders])

    return lines


def get_score_for_line(line, row_zero_score):
    start_score = row_zero_score - line[0]
    total = 0
    for j, i in enumerate(range(line[0], line[0] + line[1])):
        total += start_score - j
    return total


def get_scores_for_lines(lines, row_zero_score):
    return sum([get_score_for_line(line, row_zero_score) for line in lines])


def get_score_for_col(index, data):
    lines = get_lines(index, data)
    return get_scores_for_lines(lines, len(data))

def rotate(data, direction):
    if direction == 'N':
        for i in range(0,len(data[0])):
            line_start = -1
            boulders = 0
            for j in range(0, len(data)):
                c = data[j][i]
                if c == 'O':
                    boulders += 1
                elif c == '#':
                    for b in range(line_start + 1, j):
                        if b-line_start <= boulders:
                            data[b][i] = 'O'
                        else:
                            data[b][i] = '.'
                    line_start = j
                    boulders = 0
            for b in range(line_start + 1, len(data)):
                if b-line_start <= boulders:
                    data[b][i] = 'O'
                else:
                    data[b][i] = '.'
    elif direction == 'N':
        for i in range(0,len(data[0])):
            line_start = len(data)
            boulders = 0
            for j in range(len(data), 0, -1):
                c = data[j][i]
                if c == 'O':
                    boulders += 1
                elif c == '#':
                    for b in range(line_start - 1, j, -1):
                        if line_start - b <= boulders:
                            data[b][i] = 'O'
                        else:
                            data[b][i] = '.'
                    line_start = j
                    boulders = 0
            for b in range(line_start - 1, 0, -1):
                if line_start - b <= boulders:
                    data[b][i] = 'O'
                else:
                    data[b][i] = '.'

    elif direction == 'W':
        for i in range(0,len(data)):
            line_start = -1
            boulders = 0
            for j in range(0, len(data[i])):
                c = data[i][j]
                if c == 'O':
                    boulders += 1
                elif c == '#':
                    for b in range(line_start + 1, j):
                        if b - line_start <= boulders:
                            data[i][b] = 'O'
                        else:
                            data[i][b] = '.'
                    line_start = j
                    boulders = 0
                    
            for b in range(line_start + 1, len(data[i])):
                if b - line_start <= boulders:
                    data[i][b] = 'O'
                else:
                    data[i][b] = '.'
    elif direction == 'E':
        for i in range(0,len(data)):
            line_start = len(data)
            boulders = 0
            for j in range(len(data[i])-1, 0, -1):
                c = data[i][j]
                if c == 'O':
                    boulders += 1
                elif c == '#':
                    for b in range(line_start -1, j, -1):
                        if b - line_start <= boulders:
                            data[b][i] = 'O'
                        else:
                            data[b][i] = '.'
                    line_start = j
                    boulders = 0

            for b in range(line_start -1, 0 , -1):
                if b - line_start <= boulders:
                    data[i][b] = 'O'
                else:
                    data[i][b] = '.'
    return data

def hash_it(direction, adjusted_data):
    unpacked = []
    for a in adjusted_data:
        unpacked+= a
    return hash((direction, *unpacked))

def adjust_data(data, cycles):
    data_cache = {}
    cache_ref = {}
    directions = ['N','W','S','E',]
    i = 0
    adjusted = data
    while i < cycles:
        from_direction = directions[(i-1)%4]
        hashed = hash_it(from_direction, adjusted)
        if hashed in data_cache:
            i, adjusted = lookup_from_cache(i, data_cache, cache_ref, hashed, cycles)
        else:
            if i > 0:
                data_cache[hashed] = i
                cache_ref[i] = adjusted
            adjusted = rotate(adjusted, directions[i%4])
            i+=1
    return adjusted

def lookup_from_cache(i, data_cache, cache_ref, hashed, cycles):
    index = data_cache[hashed] # 6
    since_then = i - index # 9 - 6 == repeat every 3
    to_end = cycles - i # 100 - 9 == 91
    remainder = to_end % since_then # == 1

    trial_end = index + remainder # 7
    if trial_end in cache_ref:
        return cycles, cache_ref[trial_end]
    else:
        i = cycles - remainder # == 99
        return i, cache_ref[index]

def part_1(data):
    total = 0
    for i, _ in enumerate(data[0]):
        total += get_score_for_col(i, data)

    print(f"Part 1: {total}")
    return total

def data_to_matrix(data):
    matrix = []
    for d in data:
        matrix.append([])
        for c in d:
            matrix[-1].append(c)
    return matrix

def part_2(data):
    total = 0
    data = data_to_matrix(data)
    adjusted_data = adjust_data(data, 1000000000)
    for i, _ in enumerate(adjusted_data[0]):
        total += get_score_for_col(i, adjusted_data)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
