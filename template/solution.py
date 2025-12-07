from AocCommon import get_data, get_data_blob, data_to_list_grid, split_data_with_regex

def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data()
#data = get_data_blob()
#data = data_to_list_grid()
#data = split_data_with_regex(data, "add pattern")

##########################################################################

def solve_part_1(data):
    pass

def solve_part_2(data):
    pass

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
