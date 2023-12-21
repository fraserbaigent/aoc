import solution

test_data = [
    l.strip()
    for l in """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........
""".split(
        "\n"
    )
    if len(l.strip())
]


def test_part_1():
    expected_part_1 = 16
    assert solution.part_1(test_data, 6) == expected_part_1


def test_part_2():
    test_cases = [
        [6, 16],
        [10, 50],
        [50, 1594],
        [100, 6536],
        [500, 167004],
        [1000, 668697],
        [5000, 16733044],
    ]
    for t in test_cases:
        assert solution.part_2(test_data, t[0]) == t[1]
