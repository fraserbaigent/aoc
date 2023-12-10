import re


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################

card_re = re.compile("^Card ([ \\d]+)\\: (.*) \\| (.*)$")


def read_card(card):
    res = card_re.match(card)
    card_no = int(res.groups()[0])

    numbers = [int(i.strip()) for i in res.groups()[1].strip().split(" ") if len(i) > 0]
    my_numbers = [
        int(i.strip()) for i in res.groups()[2].strip().split(" ") if len(i) > 0
    ]

    return card_no, numbers, my_numbers


def points_from_card(card):
    card_no, numbers, my_numbers = read_card(card)

    exponent = 0
    for m in my_numbers:
        if m in numbers:
            exponent += 1
    return 2 ** (exponent - 1) if exponent > 0 else 0


def part_1(data):
    total = 0
    for d in data:
        total += points_from_card(d)
    print(f"Part 1: {total}")
    return total


def part_2(data):
    card_count = [1 for i in data]
    for index, (count, card) in enumerate(zip(card_count, data)):
        card_no, numbers, my_numbers = read_card(card)
        wins = 0
        for m in my_numbers:
            if m in numbers:
                wins += 1
        for i in range(index + 1, min(len(card_count), index + wins + 1)):
            card_count[i] += card_count[index]

    total = sum(card_count)
    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
