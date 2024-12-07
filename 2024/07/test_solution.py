import solution
test_data = [l.strip() for l in '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''.split('\n') if len(l.strip())]

def test_part_1():
    expected_part_1 = 3749
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 11387
    assert solution.part_2(test_data) == expected_part_2
