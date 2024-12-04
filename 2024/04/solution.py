from AocCommon import data_to_list_grid, get_data

data = get_data()
data = data_to_list_grid(data)

##########################################################################


def solve_part_1(data):
    word = "XMAS"
    mapping = {i: set() for i in word}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] in mapping:
                mapping[data[y][x]].add((x, y))

    good = 0
    dirs = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
    for x0, y0 in mapping[word[0]]:
        for dx, dy in dirs:
            this_good = True
            for i in range(1, len(word)):
                x = x0 + dx * i
                y = y0 + dy * i
                if (
                    x < 0
                    or x >= len(data[0])
                    or y < 0
                    or y >= len(data)
                    or data[y][x] != word[i]
                ):
                    this_good = False
                    break
            if this_good == True:
                good += 1
    return good


def solve_part_2(data):
    total = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "A":
                good = True
                for i in [-1, 1]:
                    x1 = x - 1
                    y1 = y + i
                    x2 = x + 1
                    y2 = y - i
                    if (
                        x1 < 0
                        or x2 >= len(data[0])
                        or y1 < 0
                        or y2 < 0
                        or y1 >= len(data)
                        or y2 >= len(data)
                    ):
                        good = False
                        break

                    c1 = data[y1][x1]
                    c2 = data[y2][x2]

                    if c1 == "M" and c2 == "S":
                        continue
                    elif c1 == "S" and c2 == "M":
                        continue
                    else:
                        good = False
                        break
                if good:
                    total += 1
    return total


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
