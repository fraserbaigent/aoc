from AocCommon import get_data

data = [[int(d) for d in d_i] for d_i in get_data()]

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

    def hash(self):
        return hash((self.x, self.y, self.z, self.direction, self.score))


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


def try_2(data):
    min_z = 4
    max_z = 10
    grid = [
        [{d: {j: None for j in range(0, max_z + 1)} for d in pairs} for i in d]
        for d in data
    ]
    next_move = [Move(0, 0, 0, ">", 0), Move(0, 0, 0, "v", 0)]
    seen_moves = set()
    while len(next_move):
        next_move = sorted(next_move, key=lambda m: m.score)
        move = next_move.pop(0)
        d = move.direction
        delta = deltas[d]
        x = move.x + delta[0]
        y = move.y + delta[1]
        z = move.z + 1

        if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
            continue

        existing_scores = grid[y][x][d]
        score_to_add = data[y][x]
        new_score = move.score + score_to_add
        if existing_scores[z] is None or existing_scores[z] > new_score:
            existing_scores[z] = new_score
            for d_i in deltas:
                if pairs[d] == d_i:
                    continue  # can't go backwards

                if d_i != d and z >= min_z:  # we're allowed to go left and right
                    move_to_add = Move(x, y, 0, d_i, new_score)
                elif (
                    d_i == d and z < max_z
                ):  # keep going - range check for max is above
                    move_to_add = Move(x, y, z, d_i, new_score)
                else:
                    continue
                move_hash = move_to_add.hash()
                if move_hash not in seen_moves:
                    next_move.append(move_to_add)
                    seen_moves.add(move_hash)

    return grid


def part_1(data):
    min_z = 0
    max_z = 3
    total = None
    mapping = [
        [{d_i: [None for i in range(0, max_z)] for d_i in deltas} for _ in d]
        for d in data
    ]
    result = traverse(data, mapping, min_z, max_z)
    last = result[len(result) - 1][len(result[0]) - 1]
    for v in ["v", ">"]:
        for d_i in last[v]:
            if d_i is not None and (total is None or total > d_i):
                total = d_i
    print(f"Part 1: {total}")
    return total


def part_2(data):
    result = try_2(data)
    last = result[len(result) - 1][len(result[0]) - 1]
    min_z = 4
    total = None
    for v in ["v", ">"]:
        for k, d_i in last[v].items():
            if k >= min_z and d_i is not None and (total is None or total > d_i):
                total = d_i

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    #    part_1(data)
    part_2(data)
