import solution
test_data = [l.strip() for l in '''
'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = "4,6,3,5,6,3,5,2,1,0"
    assert solution.solve_part_1(729,0,0,[0,1,5,4,3,0]) == expected_part_1

def test_part_2():
    expected_part_2 = "0,3,5,4,3,0"
    assert solution.solve_part_2([0,3,5,4,3,0]) == expected_part_2
