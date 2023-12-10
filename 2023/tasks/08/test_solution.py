import solution
test_data = [l.strip() for l in '''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''.split('\n') if len(l.strip())]

test_data_2 = [l.strip() for l in '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''.split('\n') if len(l.strip())]


def test_part_1():
    expected_part_1 = 6
    assert solution.part_1(test_data) == expected_part_1

def test_part_2():
    expected_part_2 = 6
    assert solution.part_2(test_data_2) == expected_part_2
