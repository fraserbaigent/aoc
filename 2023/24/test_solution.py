import solution
test_data = [l.strip() for l in '''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3                                
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 2
    assert solution.part_1(test_data, (7,27)) == expected_part_1

def test_part_2():
    expected_part_2 = 0
    assert solution.part_2(test_data) == expected_part_2
