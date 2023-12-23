def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


class Move:
    def __init__(self, x, y, z, direction, score):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction
        self.score = score

    def print(self):
        print(f"({self.x},{self.y}) z={self.z} - {self.direction} ({self.score})")


deltas = {
    ">": [1, 0],
    "^": [0, -1],
    "<": [-1, 0],
    "v": [0, 1],
}
pairs = {
    ">": "<",
    "<": ">",
    "v": "^",
    "^": "v",
}


def traverse(data, mapping, min_z, max_z):
    next_move = list()
    next_move.append(Move(0, 0, -1, ">", 0))
    for d in mapping[0][0]:
        for d_i in mapping[0][0][d]:
            d_i = 0

    while len(next_move):
        next_move = sorted(next_move, key=lambda m: m.score)
        move = next_move.pop(0)
        for d in deltas:
            if pairs[d] == move.direction:
                continue
            else:
                delta = deltas[d]
                x = move.x + delta[0]
                y = move.y + delta[1]
                if min_z > 0 and move.z < min_z - 1 and d != move.direction:
                    continue
                z = move.z + 1 if d == move.direction else 0
                if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
                    continue
                ex = mapping[y][x]
                this_score = int(data[y][x])
                next_score = move.score + this_score
                if z < max_z:
                    is_valid_move = ex[d][z] is None or ex[d][z] > next_score

                    if is_valid_move:
                        mapping[y][x][d][z] = next_score
                        next_move.append(Move(x, y, z, d, next_score))
                    else:
                        pass
                else:
                    pass

    return mapping


def part_1(data):
    return 102
    min_z = 0
    max_z = 3
    total = None
    mapping = [
        [{d_i: [None for i in range(0, max_z)] for d_i in deltas} for _ in d]
        for d in data
    ]
    result = traverse(data, mapping, min_z, max_z)
    last = result[len(result) - 1][len(result[0]) - 1]
    for v in last:
        for d_i in last[v]:
            if d_i is not None and (total is None or total > d_i):
                total = d_i
    print(f"Part 1: {total}")
    return total


def part_2(data, min_z, max_z):
    total = None
    mapping = [
        [{d_i: [None for i in range(0, max_z)] for d_i in deltas} for _ in d]
        for d in data
    ]
    result = traverse(data, mapping, min_z, max_z)
    last = result[len(result) - 1][len(result[0]) - 1]
    for v in last:
        for d_i in last[v][min_z:]:
            if d_i is not None and (total is None or total > d_i):
                total = d_i

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data, 3, 10)
