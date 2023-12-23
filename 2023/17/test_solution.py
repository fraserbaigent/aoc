import solution

test_data = [
    l.strip()
    for l in """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".split(
        "\n"
    )
    if len(l.strip())
]

test_data_2 = [
    l.strip()
    for l in """
111111111111
999999999991
999999999991
999999999991
999999999991
""".split(
        "\n"
    )
    if len(l.strip())
]

my_test =[    l.strip()
    for l in """
11129999999
99129999999
99111999999
99921999999
99991111111
""".split(
        "\n"
    )
    if len(l.strip())
]
def test_part_1():
    expected_part_1 = 102
    assert solution.part_1(test_data) == expected_part_1


def test_part_2():
    data_to_use = [[int(d) for d in d_i] for d_i in test_data]
    assert solution.part_2(data_to_use) == 94

    data_to_use = [[int(d) for d in d_i] for d_i in test_data_2]
    assert solution.part_2(data_to_use) == 71
