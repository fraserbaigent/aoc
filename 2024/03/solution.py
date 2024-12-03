import re
#from AocCommon import get_data_blob
import AocCommon
print(dir(AocCommon))
data = AocCommon.get_data_blob()

##########################################################################


def solve_part_1(data):
    ress = re.findall("mul\\(([0-9]+),([0-9]+)\\)", "".join(data))
    total = 0
    for res in ress:
        r = [int(r) for r in res]
        total += r[0] * r[1]
    return total


def solve_part_2(data):
    ress = re.findall(
        "(mul\\(([0-9]+),([0-9]+)\\)|do\\(\\)|don\\'t\\(\\))", "".join(data)
    )
    total = 0
    on = True
    for res in ress:
        if on and "mul" in res[0]:
            r = [int(r) for r in res[1:]]
            total += r[0] * r[1]
        if "do" in res[0]:
            on = True
        if "don't" in res[0]:
            on = False
    return total


def part_1(data):
    print(data)
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
