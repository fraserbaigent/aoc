import solution
test_data = [l.strip() for l in '''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 114
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 2
    assert solution.part_2(test_data) == expected_part_2
