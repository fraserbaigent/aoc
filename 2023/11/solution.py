def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################


def parse_map(data):
    empty_rows = list()
    empty_columns = list()
    column_is_empty = [True for i in data[0]]
    base_coordinates = list()
    for i, d in enumerate(data):
        if "#" not in d:
            empty_rows.append(i)
        for j, c in enumerate(d):
            if c == "#":
                column_is_empty[j] = False
                base_coordinates.append([i, j])
    for i, c in enumerate(column_is_empty):
        if c == True:
            empty_columns.append(i)
    return base_coordinates, empty_rows, empty_columns


def get_galaxy_coordinates(data, multiplier=2):
    base_coordinates, empty_rows, empty_columns = parse_map(data)
    coordinates = list()
    for c in base_coordinates:
        y_m = 0
        x_m = 0
        for e in empty_rows:
            if e < c[0]:
                y_m += multiplier - 1
            else:
                break
        for e in empty_columns:
            if e < c[1]:
                x_m += multiplier - 1
            else:
                break
        fixed_coordinate = [c[0] + y_m, c[1] + x_m]
        coordinates.append(fixed_coordinate)
    return coordinates


def get_galaxy_pairs(galaxy_coordinates):
    pairs = list()
    for i in range(0, len(galaxy_coordinates)):
        for j in range(i + 1, len(galaxy_coordinates)):
            pairs.append((galaxy_coordinates[i], galaxy_coordinates[j]))
    return pairs


def get_distance_between(pair_tuple):
    dx = pair_tuple[0][1] - pair_tuple[1][1]
    dy = pair_tuple[0][0] - pair_tuple[1][0]

    return abs(dx) + abs(dy)


def part_1(data):
    total = 0
    galaxy_coordinates = get_galaxy_coordinates(data)
    pairs = get_galaxy_pairs(galaxy_coordinates)
    for pair in pairs:
        result = get_distance_between(pair)
        total += result
    print(f"Part 1: {total}")
    return total


def part_2(data, multiplier=1000000):
    total = 0
    galaxy_coordinates = get_galaxy_coordinates(data, multiplier)
    pairs = get_galaxy_pairs(galaxy_coordinates)
    for pair in pairs:
        result = get_distance_between(pair)
        total += result
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
