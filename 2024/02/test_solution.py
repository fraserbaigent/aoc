import solution
test_data = [l.strip() for l in '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9                                
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 2
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 4
    assert solution.part_2(test_data) == expected_part_2
