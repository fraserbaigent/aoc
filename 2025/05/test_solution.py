import solution

data_raw = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
test_data = solution.parse_data(data_raw.split("\n"))

def test_part_1():
    expected_part_1 = 3
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 14
    assert solution.part_2(test_data) == expected_part_2
