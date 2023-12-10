import solution

test_data = [l.strip() for l in '''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
                                
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 8
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    test_str = [
        i.strip()
        for i in """
. . . . F - 7
 . F - - J . |
 F J . F - - J
 | . . | . . .
 L - - J . . .
""".replace(
        " ", ""
    ).split(
        "\n"
    )
    if i.strip() != ""
    ]
    rows = [[v_i for v_i in v] for v in test_str]

    assert solution.get_pt2_result(rows) == 4
    
def test_spots():
    start_spots = [
        ((0,2),(1,0)),
        ((0,2),(0,1)),
        ((0,2),(-1,0)),
        ((0,2),(0,-1)),
        ]
    assert sorted(solution.get_surrounding_spots((0,2), None, test_data)) == sorted(start_spots)

    assert solution.get_surrounding_spots((0,4),(0,1),test_data) == [((0,4),(1,0))]

    assert solution.get_surrounding_spots((0,4),(-1,0),test_data) == [((0,4),(0,-1))]

    assert solution.get_surrounding_spots((1,4),(1,0),test_data) == [((1,4),(0,-1))]

    assert solution.get_surrounding_spots((1,4),(0,1),test_data) == [((1,4),(-1,0))]

