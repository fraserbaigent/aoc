def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################

def get_mappings(data):

    mappings = {}
    for d in data:
        f, t = tuple(d.split("-"))
        if f not in mappings:
            mappings[f] = set()
        if t not in mappings:
            mappings[t] = set()
        mappings[f].add(t)
        mappings[t].add(f)
    return mappings

def solve_part_1(data):
    mappings = get_mappings(data)

    sets = set()
    for m, v in mappings.items():
        v = list(v)
        for i in range(0, len(v) - 1):
            for j in range(i + 1, len(v)):
                if v[i] in mappings[v[j]]:
                    sets.add(tuple(sorted([m, v[i], v[j]])))

    total = 0
    for s in sets:
        if len(s) != 3:
            continue
        for s_ in s:
            if s_[0] == "t":
                print(s)
                total += 1
                break
    return total


def solve_part_2(data):
    sets = set()
    for m,v in mappings.items():
        pass

    m = []
    for s in sets:
        if len(s) > m:
            m=s
    return ','.join(sorted(list(m)))
    


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
