import solution
test_data = [l.strip() for l in \
'''
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 46
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 0
    assert solution.part_2(test_data) == expected_part_2
