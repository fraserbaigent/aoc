import solution
test_data = [l.strip() for l in '''
'''.split('\n') if len(l.strip())]

def test_part_1():
    test_data = "125 17".split()
    assert solution.solve_part_1(test_data, 6) == 22
    assert solution.solve_part_1(test_data, 25) == 55312

def test_part_2():
    expected_part_2 = 0
    assert solution.part_2(test_data) == expected_part_2
