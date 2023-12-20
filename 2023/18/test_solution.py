from AocCommon import split_data_with_regex

import solution

test_data = [
    l.strip()
    for l in """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split(
        "\n"
    )
    if len(l.strip())
]
test_data = split_data_with_regex(
    test_data,
    "^(\\w) (\\d+) \\(\\#(\\w+)(\\d{1})\\)$",
    types=(str, int, str, int),
)


def test_part_1():
    return
    expected_part_1 = [10, 10, 10, 10, 8, 6, 8, 5, 7, 6, 6]
    result = solution.part_1(test_data)
    i = 0
    for e, r in zip(expected_part_1, result):

        if e != r:
            print(f"{i:>2}: {e} not found - got {r}")
        i += 1

    assert expected_part_1 == result


def test_part_2():
    expected_part_2 = 952408144115
    assert solution.part_2(test_data) == expected_part_2
