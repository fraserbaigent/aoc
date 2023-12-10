import re
from functools import cmp_to_key


def get_data(data_file) -> list:
    with open(data_file, "r") as infile:
        return [l.strip() for l in infile.readlines()]


data = get_data("data.dat")

##########################################################################
hand_re = re.compile("^(.*) (\\d+)$")
scores = {
    1: 7,
    2: {4: 6, 3: 5},
    3: {
        3: 4,
        2: 3,
    },
    4: 2,
    5: 1,
}
card_scores = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def get_hand_score(hand):
    card = hand[0]
    cards = dict()
    for c in card:
        if c not in cards:
            cards[c] = 0
        cards[c] += 1
    cards = sorted(cards.values(), reverse=True)
    score_1 = scores[len(cards)]
    if isinstance(score_1, dict):
        score = score_1[cards[0]]
    else:
        score = score_1
    return score


def get_hand_score_pt2(hand):
    card = hand[0]
    cards = dict()
    jokers = 0
    for c in card:
        if c == "J":
            jokers += 1
            continue
        if c not in cards:
            cards[c] = 0
        cards[c] += 1
    cards = sorted(cards.values(), reverse=True)
    score_1 = scores[len(cards) if len(cards) > 0 else 1]
    if isinstance(score_1, dict):
        score = score_1[cards[0] + jokers]
    else:
        score = score_1
    return score


def parse_hand(line):
    res = hand_re.match(line)
    return [res.groups()[0], int(res.groups()[1])]


def compare_hand_strength(left, right):
    for l, r in zip(left[0], right[0]):
        l_score = card_scores[l]
        r_score = card_scores[r]
        if l_score > r_score:
            return 1
        elif r_score > l_score:
            return -1
    return 0


def compare_hands(left, right):
    if left[0] == right[0]:
        return 0

    if card_scores["J"] > 0:
        left_score = get_hand_score(left)
        right_score = get_hand_score(right)
    else:
        left_score = get_hand_score_pt2(left)
        right_score = get_hand_score_pt2(right)
    if left_score > right_score:
        return 1
    if right_score > left_score:
        return -1
    return compare_hand_strength(left, right)


def part_1(data):
    total = 0
    parsed_hands = [parse_hand(l) for l in data]
    sorted_parsed_hands = sorted(parsed_hands, key=cmp_to_key(compare_hands))
    for i, s in enumerate(sorted_parsed_hands):
        total += (i + 1) * s[1]
    print(f"Part 1: {total}")
    return total


def part_2(data):
    card_scores["J"] = -1
    total = 0
    parsed_hands = [parse_hand(l) for l in data]
    sorted_parsed_hands = sorted(parsed_hands, key=cmp_to_key(compare_hands))
    for i, s in enumerate(sorted_parsed_hands):
        total += (i + 1) * s[1]

    print(f"Part 2: {total}")
    return total


if __name__ == "__main__":
    part_1(data)
    part_2(data)
