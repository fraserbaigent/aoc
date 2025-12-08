from AocCommon import data_to_list_grid, get_data, get_data_blob, split_data_with_regex
from intervaltree import IntervalTree


def parse_data(lines):
    spans = []
    ingredients = []
    flip = False
    for l in lines:
        l = l.strip()
        if l == "":
            flip = True
            continue
        if flip == False:
            spans.append(tuple([int(i) for i in l.split("-")]))
        else:
            ingredients.append(int(l))
    return sorted(spans, key=lambda k: k[0]), ingredients


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        lines = infile.readlines()
    return parse_data(lines)


data = get_data("data.dat")

##########################################################################


def solve_part_1(data):
    spans, vals = data
    tree = IntervalTree()
    for i, (start, end) in enumerate(spans):
        tree[start : end + 1] = i

    total = 0
    for v in vals:
        if len(tree.at(v)):
            total += 1
    return total


def solve_part_2(data):
    spans, vals = data
    tree = IntervalTree()
    for i, (start, end) in enumerate(spans):
        tree[start : end + 1] = i

    tree.merge_overlaps()
    total = 0
    for span in tree:
        total += span.end - span.begin
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
