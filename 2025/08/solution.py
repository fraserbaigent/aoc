from AocCommon import data_to_list_grid, get_data, get_data_blob, split_data_with_regex


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")
# data = get_data_blob()
data = data_to_list_grid(data, ",", int)
# data = split_data_with_regex(data, "add pattern")

##########################################################################


def pythagoras(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5


def get_distance_map(data):
    mappings = {}
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            mappings[(i, j)] = pythagoras(data[i], data[j])
    return mappings


def solve_part_1(data, sorted_distances, limit):
    mappings = {}
    groups = []
    for i in range(0, len(data)):
        groups.append([i])
        mappings[i] = i
    i = 0
    for (left, right), distance in sorted_distances.items():
        if i >= limit:
            break
        i += 1
        if left in mappings and right in mappings and mappings[left] == mappings[right]:
            continue
        elif left in mappings and right in mappings:
            old_mapping = mappings[right]
            for m in groups[old_mapping]:
                groups[mappings[left]].append(m)
                mappings[m] = mappings[left]
            groups[old_mapping] = []
        elif left in mappings:
            groups[mappings[left]].append(right)
            mappings[right] = mappings[left]
        elif right in mappings:
            groups[mappings[right]].append(left)
            mappings[left] = mappings[right]
    topvals = sorted([len(g) for g in groups], reverse=True)[:3]
    i = 1
    for t in topvals:
        i *= t
    return i


def solve_part_2(data, sorted_distances):
    mappings = {}
    groups = []
    for i in range(0, len(data)):
        groups.append([i])
        mappings[i] = i
    last_new_group = None
    for (left, right), distance in sorted_distances.items():
        if left in mappings and right in mappings and mappings[left] == mappings[right]:
            pass
        elif left in mappings and right in mappings:
            old_mapping = mappings[right]
            for m in groups[old_mapping]:
                groups[mappings[left]].append(m)
                mappings[m] = mappings[left]
            groups[old_mapping] = []
            last_new_group = mappings[left]
        elif left in mappings:
            groups[mappings[left]].append(right)
            mappings[right] = mappings[left]
            last_new_group = mappings[left]
        elif right in mappings:
            groups[mappings[right]].append(left)
            mappings[left] = mappings[right]
            last_new_group = mappings[left]
        if len(groups[last_new_group]) == len(data):
            return data[left][0] * data[right][0]
    topvals = sorted([len(g) for g in groups], reverse=True)[:3]
    i = 1
    for t in topvals:
        i *= t
    return i


def part_1(data, limit):
    distances = get_distance_map(data)
    sorted_distances = {
        k: distances[k] for k in sorted(distances, key=lambda k: distances[k])
    }
    total = solve_part_1(data, sorted_distances, limit)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    distances = get_distance_map(data)
    sorted_distances = {
        k: distances[k] for k in sorted(distances, key=lambda k: distances[k])
    }

    total = solve_part_2(data, sorted_distances)

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data, 1000)
    part_2(data)
