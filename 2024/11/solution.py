from AocCommon import get_data_blob

data = get_data_blob()
data = data.split()

##########################################################################


def split_stone(stone, times):
    to_add = [stone]
    next_to_add = []
    for i in range(0, times):
        while len(to_add) > 0:
            s = to_add.pop(0)
            if int(s) == 0:
                next_to_add.append("1")
            elif len(s) % 2 == 0:
                next_to_add.append(str(int(s[: len(s) // 2])))
                next_to_add.append(str(int(s[len(s) // 2 :])))
            else:
                next_to_add.append(str(int(s) * 2024))

        to_add = next_to_add
        next_to_add = []
    return to_add


def solve_with_memo(stone, index, memo):
    if (stone, index) in memo:
        return memo[(stone, index)]

    total = 0
    if index == 75:
        total = 1
    elif int(stone) == 0:
        total += solve_with_memo("1", index + 1, memo)
    elif len(stone) % 2 == 0:
        for s in [
            str(int(stone[: len(stone) // 2])),
            str(int(stone[len(stone) // 2 :])),
        ]:
            total += solve_with_memo(s, index + 1, memo)
    else:
        total += solve_with_memo(str(int(stone) * 2024), index + 1, memo)

    memo[(stone, index)] = total
    return total


def part_1(data):
    total = 0
    for d in data:
        total += len(split_stone(d, 25))
    print(f"Part 1: {total}")
    return total


def part_2(data):
    total = 0
    memo = {}
    for d in data:
        total += solve_with_memo(d, 0, memo)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
