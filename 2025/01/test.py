from solution import part_2



def test_part_2():
    test_data = [
        'L50',
        'L100',
        'R50',
        'L68',
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
        ]
    assert part_2(test_data) == 8
