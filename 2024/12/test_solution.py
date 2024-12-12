import solution

test_data = [
    [i for i in l.strip()]
    for l in """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split(
        "\n"
    )
    if len(l.strip())
]

test_data2 = [
    [i for i in l.strip()]
    for l in """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""".split(
        "\n"
    )
    if len(l.strip())
]


def test_part_1():
    expected_part_1 = 1930
    assert solution.part_1(test_data) == expected_part_1


def test_part_2():
    expected_part_2 = 1206
    assert solution.part_2(test_data) == expected_part_2



def test_part_22():
    expected_part_2 = 236
    assert solution.part_2(test_data2) == expected_part_2
    
